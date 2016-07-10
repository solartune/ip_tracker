# coding=utf-8
from __future__ import unicode_literals

import factory

from ..models import Tracker


class TrackerFactory(factory.django.DjangoModelFactory):
    """
    Factory for creating some quantity of trackers

    """

    class Meta:
        model = Tracker

    ip = factory.Sequence(lambda n: '192.168.0.{}'.format(n))
