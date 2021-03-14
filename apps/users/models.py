#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Django
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext as _
from django.contrib.auth.models import AbstractUser


VERSION = (0, 0, 2)
__author__ = 'Raul Bautista Arroyo'
__email__ = 'raulba4@gmail.com'
__date__ = '13/03/2021'
__modified__ = '13/03/2021'
__version__ = '.'.join([str(x) for x in VERSION])

COMMON_USER_DEFAULT_PHOTO = settings.COMMON_USER_DEFAULT_PHOTO


class CustomUser(AbstractUser):
    """ Common_User """

    TREATMENT_CHOICES = (
        ('C.', _('C.')),
        ('Lic.', _('Lic.')),
        ('Ing.', _('Ing.')),
        ('Mtro.', _('Mtro.')),
        ('Dr.', _('Dr.')),
    )
    USERNAME_FIELD = 'username'

    last_name = models.CharField(
        _('Apellido Paterno'), max_length=30, blank=True
    )
    mothers_last_name = models.CharField(
        _('Apellido Materno'), max_length=30, blank=True
    )
    treatment = models.CharField(
        _('Título'), max_length=5, choices=TREATMENT_CHOICES,
        blank=True, null=True, default=_('C.')
    )

    def get_full_name(self):
        """
        Returns the first_name, the last_name, the mothers_last_name
        with a space in between.
        """
        full_name = '{} {} {} {}'.format(
            self.treatment or 'C.', self.first_name, self.last_name,
            self.mothers_last_name
        )
        return full_name.strip()

    def get_first_name_and_first_lastname(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '{} {}'.format(self.first_name, self.last_name)
        return full_name.strip()

    def get_complete_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '{} {} {}'.format(
            self.first_name, self.last_name, self.mothers_last_name
        )
        return full_name.strip()

    def __str__(self):
        name = self.get_full_name() if self.first_name else self.username
        return name

    class Meta:
        verbose_name = _('Usuario')
        verbose_name_plural = _('Usuarios')
        ordering = ['-date_joined']


class Rack1User(models.Model):
    """ rack1 user model """
    user = models.ForeignKey(
        CustomUser, verbose_name=_('Usuario'),
        null=False, blank=False,
        on_delete=models.CASCADE
    )
    email = models.EmailField(
        verbose_name=_('Coreo electronico')
    )
    phone = models.CharField(
        null=False, blank=False,
        max_length=10
    )
    cellphone = models.CharField(
        null=False, blank=True,
        max_length=50
    )
    photo = models.ImageField(
        upload_to='common_user/photos/',
        default=COMMON_USER_DEFAULT_PHOTO,
        null=True, blank=True, max_length=200
    )

    class Meta:
        verbose_name = _('Usuario rack1')
        verbose_name_plural = _('Usuarios rack1')

    def __str__(self):
        return '{}'.format(self.user.get_full_name())
