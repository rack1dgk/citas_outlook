#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Django
from django.db import transaction

# Models
from .models import Rack1User, CustomUser

VERSION = (0, 0, 2)
__author__ = 'Raul Bautista Arroyo'
__email__ = 'raulba4@gmail.com'
__date__ = '13/03/2021'
__modified__ = '13/03/2021'
__version__ = '.'.join([str(x) for x in VERSION])
