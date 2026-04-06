"""
This is the starting point when a user enters a url in their web browser.

The urls is matched (by regex) and mapped to a 'view' - a Python function or
callable class that in turn (usually) makes use of a 'template' (a html file
with slots that can be replaced by dynamic content) in order to render a HTML
page to show the user.

This file includes the urls in website, webclient and admin. To override you
should modify urls.py in those sub directories.

Search the Django documentation for "URL dispatcher" for more help.

"""

from django.urls import include, path
from django.views.generic import RedirectView

# default evennia patterns
from evennia.web.urls import urlpatterns as evennia_default_urlpatterns

# add patterns
urlpatterns = [
    # compatibility aliases: forward /accounts/* to Evennia's /auth/* routes
    path(
        "accounts/login/",
        RedirectView.as_view(url="/auth/login/", permanent=False, query_string=True),
    ),
    path(
        "accounts/logout/",
        RedirectView.as_view(url="/auth/logout/", permanent=False, query_string=True),
    ),
    path(
        "accounts/register/",
        RedirectView.as_view(url="/auth/register/", permanent=False, query_string=True),
    ),
    # website
    path("", include("web.website.urls")),
    # asynchronous browser play
    path("async/", include("world.asyncplay.urls")),
    # webclient
    path("webclient/", include("web.webclient.urls")),
    # web admin
    path("admin/", include("web.admin.urls")),
    # wiki
    path("wiki/", include("world.wiki.urls")),
    # add any extra urls here:
    # path("mypath/", include("path.to.my.urls.file")),
]

# 'urlpatterns' must be named such for Django to find it.
urlpatterns = urlpatterns + evennia_default_urlpatterns
