#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Utils
import os
import logging

# Django
from django.conf import settings
from django.core.mail import EmailMessage, EmailMultiAlternatives


logger = logging.getLogger('server')


def send_mail(
    subject, message, to, cc=None,
        bcc=None, reply_to=None, list_files=None):

    try:
        email_from = settings.EMAIL_HOST_USER
        email = EmailMessage(
            subject,
            message,
            email_from,
            to=to,
            cc=cc,
            bcc=bcc,
            reply_to=reply_to
        )
        email.content_subtype = 'html'
        if list_files is not None:
            for File in list_files:
                email.attach_file(File)
        email.send()
    except Exception as error:
        logger.error('Error sending email ' + str(error))


def send_appointment_mail(
    subject, message, to, cc=None,
        bcc=None, reply_to=None, list_files=None, method_send="REQUEST"):
    """ Method for create and cancel appointment """
    try:
        headers = {
            "From": settings.EMAIL_HOST_USER,
            "MIME-Version": "1.0",
            "Content-Type": "text/calendar; method={0}; charset='UTF-8'".format(method_send),
            "Content-Transfer-Encoding": "7bit"
        }

        email_from = settings.EMAIL_HOST_USER
        email = EmailMessage(
            subject,
            message,
            email_from,
            to=to,
            cc=cc,
            bcc=bcc,
            reply_to=reply_to,
            headers=headers
        )
        email.content_subtype = 'html'
        if list_files is not None:
            for File in list_files:
                email.attach_file(File)
        email.send()
    except Exception as error:
        logger.error('Error sending email ' + str(error))