"""
Wiki models for the game content management system.
"""

from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone


class WikiCategory(models.Model):
    """
    Categories for organizing wiki pages (e.g., Setting, Factions, Rules, etc.)
    """
    name = models.CharField(max_length=100, unique=True, help_text="Category name")
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    description = models.TextField(blank=True, help_text="Brief description of this category")
    icon = models.CharField(
        max_length=50, 
        blank=True, 
        help_text="Font Awesome icon class (e.g., 'fa-book', 'fa-users')"
    )
    order = models.IntegerField(
        default=0, 
        help_text="Display order (lower numbers first)"
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='subcategories',
        help_text="Parent category for hierarchical organization"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Wiki Categories"
        ordering = ['order', 'name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('wiki:category', kwargs={'slug': self.slug})

    def get_all_pages(self):
        """Get all pages in this category and subcategories"""
        pages = list(self.pages.filter(published=True))
        for subcat in self.subcategories.all():
            pages.extend(subcat.get_all_pages())
        return pages


class WikiPage(models.Model):
    """
    Individual wiki pages containing content about the game world.
    """
    title = models.CharField(max_length=200, help_text="Page title")
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    content = models.TextField(help_text="Main content (supports Markdown)")
    summary = models.CharField(
        max_length=300,
        blank=True,
        help_text="Brief summary for listings and search results"
    )
    
    category = models.ForeignKey(
        WikiCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='pages'
    )
    
    tags = models.CharField(
        max_length=200,
        blank=True,
        help_text="Comma-separated tags for this page"
    )
    
    # Publishing controls
    published = models.BooleanField(
        default=True,
        help_text="Whether this page is visible to players"
    )
    staff_only = models.BooleanField(
        default=False,
        help_text="Only visible to staff members"
    )
    featured = models.BooleanField(
        default=False,
        help_text="Feature this page on the home page"
    )
    
    # Metadata
    created_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
        related_name='wiki_pages_created'
    )
    updated_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
        related_name='wiki_pages_updated'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # View tracking
    view_count = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['title']
        permissions = [
            ("can_edit_wiki", "Can edit wiki pages"),
            ("can_publish_wiki", "Can publish wiki pages"),
        ]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        # Generate summary from content if not provided
        if not self.summary and self.content:
            # Strip markdown and take first 200 chars
            import re
            plain = re.sub(r'[#*_`\[\]()]', '', self.content)
            self.summary = plain[:200].strip()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('wiki:page', kwargs={'slug': self.slug})

    def increment_views(self):
        """Increment view count"""
        self.view_count += 1
        self.save(update_fields=['view_count'])

    def get_tags_list(self):
        """Return tags as a list"""
        if not self.tags:
            return []
        return [tag.strip() for tag in self.tags.split(',') if tag.strip()]


class WikiRevision(models.Model):
    """
    Track revisions of wiki pages for history and rollback.
    """
    page = models.ForeignKey(
        WikiPage,
        on_delete=models.CASCADE,
        related_name='revisions'
    )
    content = models.TextField()
    summary = models.CharField(max_length=200, blank=True, help_text="Change summary")
    revised_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True
    )
    revised_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-revised_at']

    def __str__(self):
        return f"{self.page.title} - {self.revised_at.strftime('%Y-%m-%d %H:%M')}"


class WikiImage(models.Model):
    """
    Images that can be embedded in wiki pages.
    """
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='wiki/images/%Y/%m/')
    description = models.TextField(blank=True)
    uploaded_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-uploaded_at']

    def __str__(self):
        return self.title

