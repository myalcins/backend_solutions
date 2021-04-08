from django.core.cache import cache
from solution.models import NavigationRecord


def latest_update(request):
    last_update = cache.get('last_update')
    if last_update:
        return last_update
    return NavigationRecord.objects.latest('datetime').datetime