# coding=utf-8
from __future__ import unicode_literals

from django.db import IntegrityError

from rest_framework import viewsets, serializers

from .models import Tracker
from .serializers import TrackerSerializer, TrackerCreateSerializer


class TrackerViewSet(viewsets.ModelViewSet):
    """
    View set for trackers.
    Provides get, post and head actions for objects.

    """

    queryset = Tracker.objects.all()
    serializer_class = TrackerSerializer
    http_method_names = ['get', 'post', 'head']

    def get_serializer_class(self, *args, **kwargs):
        """
        Method provides special serializer for create objects

        """

        serializers = {
            'create': TrackerCreateSerializer,
        }
        return serializers.get(self.action, TrackerSerializer)

    def perform_create(self, serializer):
        """
        Method provides integrate IP address of a client

        """

        serializer.validated_data['ip'] = self.request.META.get("REMOTE_ADDR")
        try:
            super(TrackerViewSet, self).perform_create(serializer)
        except IntegrityError:
            raise serializers.ValidationError(
                'Sorry, but IP address of this client is not correct.'
            )
