#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Django
from django.conf import settings

# Utils
from datetime import timedelta, datetime
from apps.utils.utils import send_appointment_mail


VERSION = (0, 0, 4)
__author__ = 'Raul Bautista Arroyo'
__email__ = 'raulba4@gmail.com'
__date__ = '06/01/2021'
__modified__ = '06/01/2021'
__version__ = '.'.join([str(x) for x in VERSION])


def format_for_dates(date_formater):
    send_date = "{}".format(
        datetime.strptime(
            date_formater,
            "%Y-%m-%d"
        ).date()
    ).replace("-", "")
    return send_date


def format_for_hours(hour_formater):
    send_hour = "{}".format(
        datetime.strptime(
            hour_formater,
            "%H:%M"
            ).time()
        ).replace(":", "")
    return send_hour


def create_uid_appointment(id_sinister, id_eco, date_of_appointment):
    import hashlib
    dates_and_hours = date_of_appointment.split('T')
    text_encrypt = "{}{}{}".format(id_sinister, id_eco, dates_and_hours[0])
    UID = hashlib.md5(text_encrypt.encode())
    return UID.hexdigest().upper()


def QuoteTypeOutlook(addressee, date_of_appointment, address, affair, start_time, end_time,
                     html_content, method_send, UID):
    # addressee (Destinatario); date_of_appointment (fecha de la cita); address(lugar de la cita)
    # affair (Asunto); start_time(Hora de inicio); end_time(Hora de fin);
    # html_content (HTML de la cita)
    # Method's REQUEST(crear), CANCEL(cancelar), PUBLISH(Actualizar)
    expenses_text = """BEGIN:VCALENDAR
METHOD:{9}
PRODID:Microsoft Exchange Server 2010
VERSION:2.0
BEGIN:VTIMEZONE
TZID:Central Standard Time (Mexico)
BEGIN:STANDARD
DTSTART:16010101T020000
TZOFFSETFROM:-0500
TZOFFSETTO:-0600
RRULE:FREQ=YEARLY;INTERVAL=1;BYDAY=-1SU;BYMONTH=10
END:STANDARD
BEGIN:DAYLIGHT
DTSTART:16010101T020000
TZOFFSETFROM:-0600
TZOFFSETTO:-0500
RRULE:FREQ=YEARLY;INTERVAL=1;BYDAY=1SU;BYMONTH=4
END:DAYLIGHT
END:VTIMEZONE
BEGIN:VEVENT
ORGANIZER;CN=Una empresa de test:mailto:{6}
ATTENDEE;ROLE=REQ-PARTICIPANT;PARTSTAT=NEEDS-ACTION;RSVP=TRUE;
CN={6}:mailto:{6}
ATTENDEE;ROLE=REQ-PARTICIPANT;PARTSTAT=NEEDS-ACTION;RSVP=TRUE;
CN={6}:mailto:{6}
DESCRIPTION: Se ha creado una nueva cita, favor de confirmar;
LANGUAGE=en-US: "";
X-ALT-DESC;FMTTYPE=text/html: {7}
UID:040000008200E00074C5B7101A82E008000000008C556565C7BDD601000000000000000
 010000000{5}

SUMMARY;LANGUAGE=en-US:{8}
DTSTART;TZID=Central Standard Time (Mexico):{0}T{3}
DTEND;TZID=Central Standard Time (Mexico):{1}T{4}
CLASS:PUBLIC
PRIORITY:5
DTSTAMP:20201124T162515Z
TRANSP:OPAQUE
STATUS:CONFIRMED
SEQUENCE:0
LOCATION;LANGUAGE=en-US:{2}
X-MICROSOFT-CDO-APPT-SEQUENCE:0
X-MICROSOFT-CDO-OWNERAPPTID:2118881932
X-MICROSOFT-CDO-BUSYSTATUS:TENTATIVE
X-MICROSOFT-CDO-INTENDEDSTATUS:BUSY
X-MICROSOFT-CDO-ALLDAYEVENT:FALSE
X-MICROSOFT-CDO-IMPORTANCE:1
X-MICROSOFT-CDO-INSTTYPE:0

X-MICROSOFT-DONOTFORWARDMEETING:FALSE
X-MICROSOFT-DISALLOW-COUNTER:FALSE

BEGIN:VALARM
DESCRIPTION:REMINDER
TRIGGER;RELATED=START:-PT15M
ACTION:DISPLAY
END:VALARM
END:VEVENT
END:VCALENDAR
         """.format(
             format_for_dates(date_of_appointment), # 0
             format_for_dates(date_of_appointment), # 1
             address, # 2
             format_for_hours(start_time), # 3
             format_for_hours(end_time), # 4
             UID, # 5
             settings.EMAIL_HOST_USER, # 6
             html_content, # 7
             affair, # 8
             method_send # 9
            )

    email_message = expenses_text
    send_appointment_mail(
        affair,
        email_message,
        [],
        addressee,  # mail_list
        method_send=method_send
        )


def desing_of_the_appointment(title_mail_quote, date, UID, duration, method_send="REQUEST"):
    """ Method for created a appointment to sininester and affected"""
    # duration in minutes(duración de las cita en minutos)

    # created to format of dates
    dates_and_hours = date.split('T')

    # fecha de la cita
    date_appointment = dates_and_hours[0]

    # hora de la cita
    hour_appointment = dates_and_hours[1]

    # finish of quote (final de la cita)
    second_hour_prepare = (datetime.strptime(hour_appointment, "%H:%M") + timedelta(minutes=int(duration))).time()
    hour_finish_appointment = "{0}:{1}".format(
        second_hour_prepare.hour,
        second_hour_prepare.minute
    )

    # affair (asunto)
    affair_send = "Se fijó la cita para: {}".format(title_mail_quote)

    # html fills up of the message (HTML que se enviará en el mensaje)
    title_appointment = "Se ha creado una nueva cita, favor de confirmar"
    class_appointment = ""
    if method_send == "CANCEL":
        title_appointment = "La fecha u hora de la cita ha cambiado"
        class_appointment = "style='color: #BA1504'"
    html_content = """
        <P DIR=LTR>
            <SPAN LANG="es-mx">
                <FONT FACE="Calibri" {1} >{0}</FONT>
            </SPAN>
        </P>
        <table style="text-align: center">
            <tr>
                <td style="background-color: #85D36A; font-weight: bold;">
                    <FONT FACE="Calibri" >Datos de la cita:</FONT>
                </td>
                <td><FONT FACE="Calibri" >{3}</FONT></td>
            </tr>
            <tr>
                <td style="background-color: #85D36A;  font-weight: bold;">
                    <FONT FACE="Calibri" >Fecha de la cita:</FONT>
                </td>
                <td><FONT FACE="Calibri" >{2}</FONT></td>
            </tr>
        </table>
        """.format(
            title_appointment,
            class_appointment,
            date_appointment,
            "Más datos de la cita"
        )

    # send appointment (Enviar cita)
    QuoteTypeOutlook(
        ["raulba4@outlook.com"], date_appointment,
        "Una dirección, calle tal, No. tal, ciudad tel.", affair_send,
        hour_appointment, hour_finish_appointment,
        html_content, method_send, UID,
    )