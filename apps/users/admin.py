#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Django
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

# Models
from .models import Rack1User

VERSION = (0, 0, 1)
__author__ = 'Raul Bautista Arroyo'
__email__ = 'raulba4@gmail.com'
__date__ = '13/03/2021'
__modified__ = '13/03/2021'
__version__ = '.'.join([str(x) for x in VERSION])


class Rack1UserAdmin(UserAdmin):
    search_fields = ('username', 'email')
    list_display = (
        'username', 'email', 'first_name', 'last_name',
        'mothers_last_name', 'is_staff', 'is_active'
    )
    list_filter = ('is_active', 'is_staff')
    filter_horizontal = ()
    fieldsets = (
        (
            None,
            {
                'fields': ('username', 'email', 'password')
            }
        ),
        (
            'Personal Info',
            {
                'classes': ('wide', 'extrapretty'),
                'fields': (
                    'treatment',
                    'first_name',
                    'last_name',
                    'mothers_last_name'
                )
            }
        ),
        (
            'Permissions',
            {
                'classes': ('collapse',),
                'fields':
                (
                    'is_active', 'is_staff',
                    'is_superuser', 'groups', 'user_permissions'
                )
            }
        ),
        (
            'Important dates',
            {
                'classes': ('collapse',),
                'fields': ('last_login', 'date_joined')
            }
        ),
    )


admin.site.register(Rack1User)
admin.site.register(get_user_model(), Rack1UserAdmin)
