from django.db import models

class Heater(models.Model):
    name = models.CharField(max_length=100)
    temperature = models.FloatField()
    pressure = models.FloatField()

    def __str__(self):
        return self.name
