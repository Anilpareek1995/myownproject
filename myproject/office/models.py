from django.db import models

class Mostwanted(models.Model):
    name = models.CharField(max_length=20)
    height = models.IntegerField(default=0)
    color = models.CharField(max_length=20)
    crime_type = models.CharField(max_length=20)
    crime_area = models.CharField(max_length=20)
    victim = models.CharField(max_length=20)
    crime_spot = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='pic', blank=True)
    date = models.DateTimeField(auto_now=True)


def _str_(self):
    return self.name
