# coding=utf-8
from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible

from django.db import models


@python_2_unicode_compatible
class Tracker(models.Model):
    """
    Model for tracking clients of a site

    """

    ip = models.GenericIPAddressField("IP-адрес клиента")
    time = models.DateTimeField("Время записи", auto_now_add=True)

    class Meta:
        verbose_name = 'Трекер'
        verbose_name_plural = 'Трекеры'
        ordering = ['-time']

    def __str__(self):
        return 'IP адрес {ip}, зафиксирован {date} в {time}'.format(
            ip=self.ip, date=self.time.strftime("%d.%m.%Y"),
            time=self.time.strftime("%H:%M:%S")
        )
