#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Django
from django.urls import path

# Views
from .views import SendMail

VERSION = (0, 0, 2)
__author__ = 'Raul Bautista'
__email__ = 'raulba4@gmail.com'
__date__ = '06/01/2021'
__modified__ = '06/01/2021'
__version__ = '.'.join([str(x) for x in VERSION])

urlpatterns = [

    path(
        '',
        SendMail.as_view(),
        name='send-mail'),

]