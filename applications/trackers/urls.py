# coding=utf-8

from __future__ import unicode_literals

from rest_framework.routers import DefaultRouter

from .views import TrackerViewSet


trackers_router = DefaultRouter()
trackers_router.register(r'trackers', TrackerViewSet)
