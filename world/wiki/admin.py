"""
Django admin interface for wiki management.
"""

from django.contrib import admin
from .models import WikiPage, WikiCategory, WikiRevision, WikiImage


@admin.register(WikiCategory)
class WikiCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'parent', 'order', 'page_count']
    list_filter = ['parent']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['order', 'name']
    
    def page_count(self, obj):
        return obj.pages.count()
    page_count.short_description = 'Pages'


class WikiRevisionInline(admin.TabularInline):
    model = WikiRevision
    extra = 0
    readonly_fields = ['revised_at', 'revised_by', 'summary']
    fields = ['revised_at', 'revised_by', 'summary']
    can_delete = False
    max_num = 5
    
    def has_add_permission(self, request, obj=None):
        return False


@admin.register(WikiPage)
class WikiPageAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'category', 'published', 'staff_only', 
        'featured', 'view_count', 'updated_at', 'updated_by'
    ]
    list_filter = ['published', 'staff_only', 'featured', 'category', 'created_at']
    search_fields = ['title', 'content', 'tags']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['created_at', 'updated_at', 'view_count', 'created_by', 'updated_by']
    
    fieldsets = (
        ('Content', {
            'fields': ('title', 'slug', 'summary', 'content', 'category', 'tags')
        }),
        ('Publishing', {
            'fields': ('published', 'staff_only', 'featured')
        }),
        ('Metadata', {
            'fields': ('created_by', 'created_at', 'updated_by', 'updated_at', 'view_count'),
            'classes': ('collapse',)
        }),
    )
    
    inlines = [WikiRevisionInline]
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(WikiRevision)
class WikiRevisionAdmin(admin.ModelAdmin):
    list_display = ['page', 'revised_by', 'revised_at', 'summary']
    list_filter = ['revised_at', 'page']
    search_fields = ['page__title', 'summary', 'content']
    readonly_fields = ['page', 'revised_by', 'revised_at', 'content', 'summary']
    
    def has_add_permission(self, request):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False


@admin.register(WikiImage)
class WikiImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'uploaded_by', 'uploaded_at']
    list_filter = ['uploaded_at']
    search_fields = ['title', 'description']
    readonly_fields = ['uploaded_at', 'uploaded_by']
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.uploaded_by = request.user
        super().save_model(request, obj, form, change)

