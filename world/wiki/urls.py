"""
URL routing for the wiki system.
"""

from django.urls import path
from . import views

app_name = 'wiki'

urlpatterns = [
    # Main index
    path('', views.WikiIndexView.as_view(), name='index'),
    
    # Page operations
    path('page/<slug:slug>/', views.WikiPageDetailView.as_view(), name='page'),
    path('page/<slug:slug>/edit/', views.WikiPageUpdateView.as_view(), name='page_edit'),
    path('page/<slug:slug>/delete/', views.WikiPageDeleteView.as_view(), name='page_delete'),
    path('create/', views.WikiPageCreateView.as_view(), name='page_create'),
    
    # Category operations
    path('category/<slug:slug>/', views.WikiCategoryView.as_view(), name='category'),
    path('category/create/', views.WikiCategoryCreateView.as_view(), name='category_create'),
    path('category/<slug:slug>/edit/', views.WikiCategoryUpdateView.as_view(), name='category_edit'),
    
    # Search and listings
    path('search/', views.WikiSearchView.as_view(), name='search'),
    path('all/', views.all_pages_list, name='all_pages'),
    
    # AJAX
    path('ajax/preview/', views.ajax_page_preview, name='ajax_preview'),
]

