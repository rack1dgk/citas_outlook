#!/usr/bin/env python
# -*- coding: utf-8

""" vue-django URL Configuration """

# Django
from django.contrib import admin
from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from django.urls import path, include

# Django REST Framework
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path(
        'admin/',
        admin.site.urls
    ),

    # Documentation
    path(
        'api/v1/documentation/',
        include_docs_urls(title="API Documentation")
    ),
    # Project paths
    path(
        'api/v1/mails/',
        include(
            ('apps.mail.urls', 'mails'),
            namespace='mails'
        )
    ),
    # Static and media files
    url(
        r'^static/(?P<path>.*)$', serve,
        {'document_root': settings.STATICFILES_DIRS}),
    url(r'^media/(?P<path>.*)$', serve,
        {'document_root': settings.MEDIA_ROOT}),
]

if settings.ENV != 'dev':
    # Load VueApp files
    urlpatterns.append(path('', include('frontend.urls')))
