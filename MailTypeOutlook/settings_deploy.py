#!/usr/bin/env python
# -*- coding: utf-8

import os
from .settings import INSTALLED_APPS, ALLOWED_HOSTS, BASE_DIR, DEBUG

INSTALLED_APPS.append('webpack_loader',)
INSTALLED_APPS.append('frontend.apps.WebConfig',)

ALLOWED_HOSTS.append('*',)

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'frontend', 'vueapp', 'dist')
]

WEBPACK_LOADER = {
    'DEFAULT': {
        'CACHE': DEBUG,
        'BUNDLE_DIR_NAME': '/bundles/',
        'STATS_FILE': os.path.join(
            BASE_DIR, 'frontend', 'vueapp', 'webpack-stats.json'
        )
    }
}

INTERNAL_IPS = (
    '0.0.0.0',
    '127.0.0.1',
)
