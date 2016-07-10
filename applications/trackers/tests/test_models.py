# coding=utf-8

from django.test import TestCase
from django.db import IntegrityError

from applications.trackers.models import Tracker


class TrackerModelTest(TestCase):

    def test_create_tracker(self):
        Tracker.objects.create(ip='192.168.0.1')
        tracker = Tracker.objects.all()
        self.assertTrue(tracker)

    def test_multiple_create(self):
        Tracker.objects.bulk_create([
            Tracker(ip='192.168.0.1'),
            Tracker(ip='192.168.0.2'),
        ])
        tracker = Tracker.objects.all()
        self.assertEquals(tracker.count(), 2)

    def test_ordering(self):
        Tracker.objects.bulk_create([
            Tracker(ip='192.168.0.1'),
            Tracker(ip='192.168.1.2'),
            Tracker(ip='192.168.0.2'),
        ])
        self.assertEquals(Tracker.objects.first().ip, '192.168.0.2')

    def test_error_without_ip(self):
        with self.assertRaises(IntegrityError):
            Tracker.objects.create()

    def test_str(self):
        Tracker.objects.create(ip='192.168.0.1')
        tracker = Tracker.objects.first()
        self.assertEquals(
            tracker.__str__(),
            'IP адрес {ip}, зафиксирован {date} в {time}'.format(
                ip=tracker.ip, date=tracker.time.strftime("%d.%m.%Y"),
                time=tracker.time.strftime("%H:%M:%S")
            )
        )
