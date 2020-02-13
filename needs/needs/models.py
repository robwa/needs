from django.db import models
from django.urls import reverse


class Need(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    creation_time = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE)
    proposed_means = models.ManyToManyField('means.Means')
    proposed_patterns = models.ManyToManyField('patterns.Pattern')

    def get_absolute_url(self):
        return reverse('show-need', args=(self.pk,))
