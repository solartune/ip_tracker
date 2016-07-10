# coding=utf-8
from __future__ import unicode_literals

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from .data_factories import TrackerFactory
from ..models import Tracker


class TrackerAPITest(APITestCase):

    def setUp(self):
        TrackerFactory.create_batch(10)

    def test_show_trackers(self):
        url = reverse('api:trackers:tracker-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.data["count"], 10)

    def test_create_tracker(self):
        trackers = Tracker.objects.all()
        self.assertEqual(trackers.count(), 10)
        url = reverse('api:trackers:tracker-list')
        response = self.client.post(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        trackers = Tracker.objects.all()
        self.assertEqual(trackers.count(), 11)

    def test_except_for_corrupt_ip(self):
        url = reverse('api:trackers:tracker-list')
        response = self.client.post(url, format='json')
        tracker = Tracker.objects.first()

        print tracker.ip
