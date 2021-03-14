#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Django REST Framework
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

# Serializers
from .serializers import MailSerializer

# Utils
from ..utils.utils import send_mail
from .utils import desing_of_the_appointment, create_uid_appointment


VERSION = (0, 0, 2)
__author__ = 'Raul Bautista Arroyo'
__email__ = 'raulba4@gmail.com'
__date__ = '06/01/2021'
__modified__ = '06/01/2021'
__version__ = '.'.join([str(x) for x in VERSION])

class SendMail(GenericAPIView):
    serializer_class = MailSerializer

    def get(self, request):
        """ METHOD REQUEST """
        # send_mail("TEST", "Mail de prueba, este mail se envia al hacer un get", [], ["correo receptor", ])
        message = {'message': 'El GET si funciona; esta es la respuesta de un GET'}
        return Response(message, status=status.HTTP_200_OK)
    
    def post(self, request):
        """ METHOD POST """
        data_quote = request.data
        title_mail_quote = data_quote.get('title_mail_quote')
        date_quote = data_quote.get('date_quote')
        duration = data_quote.get('duration')
        UID = create_uid_appointment(7, 4, date_quote)
        desing_of_the_appointment(title_mail_quote, date_quote, UID, duration, method_send="REQUEST")
        message = {'message': 'Cita enviada con éxito'}
        return Response(message, status=status.HTTP_200_OK)



