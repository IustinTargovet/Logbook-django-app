from django.db import models
from django.contrib.auth.models import Permission, User

class Log(models.Model):
    user = models.ForeignKey(User, default = 1)
    log_title = models.CharField(max_length = 20)
    log_category = models.CharField(max_length = 20)
    log_date = models.DateTimeField()

    def __str__(self):
        return self.log_title

class Entry(models.Model):
    log = models.ForeignKey(Log, on_delete=models.CASCADE)
    title = models.CharField(max_length = 20)
    text = models.CharField(max_length = 500, default = "None")
    date = models.DateTimeField()

    def __str__(self):
        return self.title
