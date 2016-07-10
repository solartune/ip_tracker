# coding: utf-8
from __future__ import unicode_literals

from rest_framework import serializers

from .models import Tracker


class TrackerSerializer(serializers.ModelSerializer):
    """
    Base model serializer for trackers with all fields

    """

    class Meta:
        model = Tracker
        fields = '__all__'
        read_only_fields = ('time',)


class TrackerCreateSerializer(serializers.ModelSerializer):
    """
    Special serializer without IP fields for create objects.
    IP address will be integrated in view method.

    """

    class Meta:
        model = Tracker
        exclude = ("ip",)
        read_only_fields = ('time',)
