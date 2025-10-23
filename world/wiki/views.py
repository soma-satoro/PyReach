"""
Views for the wiki system.
"""

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q, Count
from django.http import JsonResponse

from .models import WikiPage, WikiCategory, WikiRevision
from .forms import WikiPageForm, WikiCategoryForm, WikiSearchForm


class WikiIndexView(ListView):
    """Main wiki index showing featured pages and categories"""
    model = WikiPage
    template_name = 'wiki/index.html'
    context_object_name = 'featured_pages'
    
    def get_queryset(self):
        """Get featured published pages"""
        return WikiPage.objects.filter(
            published=True,
            featured=True
        ).select_related('category', 'created_by')[:6]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get all top-level categories
        context['categories'] = WikiCategory.objects.filter(
            parent__isnull=True
        ).prefetch_related('subcategories', 'pages')
        
        # Get recently updated pages
        context['recent_pages'] = WikiPage.objects.filter(
            published=True
        ).order_by('-updated_at')[:5]
        
        # Get popular pages
        context['popular_pages'] = WikiPage.objects.filter(
            published=True
        ).order_by('-view_count')[:5]
        
        context['search_form'] = WikiSearchForm()
        return context


class WikiPageDetailView(DetailView):
    """Display a single wiki page"""
    model = WikiPage
    template_name = 'wiki/page_detail.html'
    context_object_name = 'page'
    
    def get_queryset(self):
        """Filter based on user permissions"""
        qs = WikiPage.objects.select_related('category', 'created_by', 'updated_by')
        
        # Staff can see all published pages
        if self.request.user.is_authenticated and self.request.user.is_staff:
            return qs.filter(published=True)
        
        # Regular users only see non-staff pages
        return qs.filter(published=True, staff_only=False)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = self.get_object()
        
        # Increment view count
        page.increment_views()
        
        # Get related pages (same category)
        if page.category:
            context['related_pages'] = WikiPage.objects.filter(
                category=page.category,
                published=True
            ).exclude(id=page.id)[:5]
        
        # Check if user can edit
        if self.request.user.is_authenticated:
            context['can_edit'] = (
                self.request.user.is_staff or
                self.request.user.has_perm('wiki.can_edit_wiki')
            )
        
        return context


class WikiCategoryView(DetailView):
    """Display all pages in a category"""
    model = WikiCategory
    template_name = 'wiki/category.html'
    context_object_name = 'category'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.get_object()
        
        # Get pages in this category
        pages = WikiPage.objects.filter(
            category=category,
            published=True
        ).select_related('created_by', 'updated_by')
        
        # Filter staff-only pages for non-staff
        if not (self.request.user.is_authenticated and self.request.user.is_staff):
            pages = pages.filter(staff_only=False)
        
        context['pages'] = pages
        context['subcategories'] = category.subcategories.all()
        
        return context


class WikiSearchView(ListView):
    """Search wiki pages"""
    model = WikiPage
    template_name = 'wiki/search.html'
    context_object_name = 'results'
    paginate_by = 20
    
    def get_queryset(self):
        query = self.request.GET.get('query', '').strip()
        category_id = self.request.GET.get('category', '')
        
        qs = WikiPage.objects.filter(published=True)
        
        # Filter staff-only pages
        if not (self.request.user.is_authenticated and self.request.user.is_staff):
            qs = qs.filter(staff_only=False)
        
        # Apply search query
        if query:
            qs = qs.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(summary__icontains=query) |
                Q(tags__icontains=query)
            )
        
        # Apply category filter
        if category_id:
            qs = qs.filter(category_id=category_id)
        
        return qs.select_related('category', 'created_by').order_by('-updated_at')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = WikiSearchForm(self.request.GET)
        context['query'] = self.request.GET.get('query', '')
        return context


class WikiPageCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """Create a new wiki page"""
    model = WikiPage
    form_class = WikiPageForm
    template_name = 'wiki/page_form.html'
    permission_required = 'wiki.can_edit_wiki'
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.updated_by = self.request.user
        response = super().form_valid(form)
        
        # Create initial revision
        WikiRevision.objects.create(
            page=self.object,
            content=self.object.content,
            summary="Initial creation",
            revised_by=self.request.user
        )
        
        messages.success(self.request, f'Page "{self.object.title}" created successfully!')
        return response


class WikiPageUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """Edit an existing wiki page"""
    model = WikiPage
    form_class = WikiPageForm
    template_name = 'wiki/page_form.html'
    permission_required = 'wiki.can_edit_wiki'
    
    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        
        # Save old content as revision before updating
        old_page = WikiPage.objects.get(pk=self.object.pk)
        WikiRevision.objects.create(
            page=old_page,
            content=old_page.content,
            summary=self.request.POST.get('revision_summary', 'Updated'),
            revised_by=self.request.user
        )
        
        response = super().form_valid(form)
        messages.success(self.request, f'Page "{self.object.title}" updated successfully!')
        return response


class WikiPageDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """Delete a wiki page"""
    model = WikiPage
    template_name = 'wiki/page_confirm_delete.html'
    success_url = reverse_lazy('wiki:index')
    permission_required = 'wiki.can_edit_wiki'
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Page deleted successfully!')
        return super().delete(request, *args, **kwargs)


# Category Management Views
class WikiCategoryCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """Create a new category"""
    model = WikiCategory
    form_class = WikiCategoryForm
    template_name = 'wiki/category_form.html'
    permission_required = 'wiki.can_edit_wiki'
    success_url = reverse_lazy('wiki:index')


class WikiCategoryUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """Edit a category"""
    model = WikiCategory
    form_class = WikiCategoryForm
    template_name = 'wiki/category_form.html'
    permission_required = 'wiki.can_edit_wiki'
    success_url = reverse_lazy('wiki:index')


# AJAX Views
@login_required
def ajax_page_preview(request):
    """Preview markdown rendering"""
    import markdown
    content = request.POST.get('content', '')
    html = markdown.markdown(content, extensions=['extra', 'codehilite', 'tables'])
    return JsonResponse({'html': html})


def all_pages_list(request):
    """List all pages (for navigation)"""
    pages = WikiPage.objects.filter(published=True)
    
    if not (request.user.is_authenticated and request.user.is_staff):
        pages = pages.filter(staff_only=False)
    
    pages = pages.values('title', 'slug', 'category__name').order_by('title')
    
    return render(request, 'wiki/all_pages.html', {'pages': pages})

