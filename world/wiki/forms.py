"""
Forms for wiki page creation and editing.
"""

from django import forms
from .models import WikiPage, WikiCategory


class WikiPageForm(forms.ModelForm):
    """Form for creating and editing wiki pages"""
    
    class Meta:
        model = WikiPage
        fields = [
            'title', 'slug', 'category', 'content', 'summary', 
            'tags', 'published', 'staff_only', 'featured'
        ]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter page title'
            }),
            'slug': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'auto-generated-from-title'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control wiki-editor',
                'rows': 20,
                'placeholder': 'Enter page content (Markdown supported)'
            }),
            'summary': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Brief summary (auto-generated if left blank)'
            }),
            'tags': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'tag1, tag2, tag3'
            }),
            'published': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'staff_only': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'featured': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['slug'].required = False
        self.fields['summary'].required = False


class WikiCategoryForm(forms.ModelForm):
    """Form for creating and editing wiki categories"""
    
    class Meta:
        model = WikiCategory
        fields = ['name', 'slug', 'description', 'icon', 'order', 'parent']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Category name'
            }),
            'slug': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'auto-generated-from-name'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Brief description'
            }),
            'icon': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'fa-book'
            }),
            'order': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'parent': forms.Select(attrs={
                'class': 'form-control'
            }),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['slug'].required = False


class WikiSearchForm(forms.Form):
    """Form for searching wiki pages"""
    
    query = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Search the wiki...'
        })
    )
    
    category = forms.ModelChoiceField(
        queryset=WikiCategory.objects.all(),
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )

