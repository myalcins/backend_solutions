from solution.models import NavigationRecord
from datetime import datetime, timedelta
from django.views.decorators import http, cache
from rest_framework.decorators import api_view
from rest_framework.response import Response
from solution.helpers import latest_update


def get_last_points():
    last_48_hours = datetime.now() - timedelta(hours=48)
    q = NavigationRecord.objects.filter(datetime__gte=last_48_hours).select_related('vehicle')\
        .values('latitude', 'longitude', 'vehicle__plate', 'datetime')
    return q


@cache.cache_control(no_cache=True)
@http.condition(last_modified_func=latest_update)
@api_view(('GET', 'HEAD'))
def last_points(request):
    q = get_last_points()
    return Response(q)