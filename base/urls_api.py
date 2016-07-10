from __future__ import unicode_literals

from django.conf.urls import url, include

from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from applications.trackers.urls import trackers_router


@api_view(['GET'])
def api_root(request, format=None):
    """
    Returns list of api urls when addressing to /api/ url

    """

    return Response({
        'trackers': reverse(
            'api:trackers:tracker-list', request=request, format=format
        ),
    })


urlpatterns = [
    url(r'^$', api_root, name='api-root'),
    url(r'^', include(trackers_router.urls, namespace='trackers')),
]
