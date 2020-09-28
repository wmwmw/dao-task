from django.db import models


class Task(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    url = models.URLField()
    title = models.TextField(null=True)
    description = models.TextField(null=True)
    site_name = models.TextField(null=True)
    image = models.URLField(null=True)
