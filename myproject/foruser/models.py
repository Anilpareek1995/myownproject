from django.db import models



class Post(models.Model):
    email = models.EmailField(max_length=20)
    name = models.CharField(max_length=20)
    write_post = models.CharField(max_length=100)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zip = models.IntegerField


def _str_(self):
    return self.name

