from django.db import models


class Bin(models.Model):
    id = models.AutoField(primary_key=True)
    latitude = models.FloatField()
    longitude = models.FloatField()


class Operation(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    collection_frequency = models.IntegerField()
    last_collection = models.DateTimeField()

    bin = models.ForeignKey(Bin, on_delete=models.CASCADE,
        related_name="operations")
