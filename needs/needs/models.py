from django.db import models


class Need(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    creation_time = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE)
