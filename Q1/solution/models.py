from django.db import models


class Vehicle(models.Model):
    id = models.AutoField(primary_key=True)
    plate = models.CharField(max_length=20)


class NavigationRecord(models.Model):
    id = models.AutoField(primary_key=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    datetime = models.DateTimeField()

    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE,
        related_name='navigation_records')
