from solution.models import NavigationRecord
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.cache import cache


@receiver(post_save, sender=NavigationRecord, dispatch_uid="unique")
def update_last_update(sender, instance, created, **kwargs):
    if created:
        cache.set('last_update', instance.datetime)