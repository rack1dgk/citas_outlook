#!/usr/bin/env python
# -*- coding: utf-8 -*-

# REST
from rest_framework import serializers

VERSION = (0, 0, 1)
__author__ = "Raul Bautista"
__mail__ = "raulba4@gmail.com"
__date__ = "06/01/2021"
__modified__ = "06/01/2021"
__version__ = ".".join([str(x) for x in VERSION])


class MailSerializer(serializers.Serializer):
    title_mail_quote = serializers.CharField(max_length=30)
    date_quote = serializers.DateTimeField()
    duration = serializers.IntegerField()

