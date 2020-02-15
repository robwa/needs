from django.db import models
from django.urls import reverse


class Activity(models.Model):
    creation_time = models.DateTimeField(auto_now_add=True)
    result_need = models.ForeignKey(
            'needs.Need', on_delete=models.CASCADE, related_name='proposed_activities')
    pattern = models.ForeignKey('patterns.Pattern', on_delete=models.PROTECT)

    #def get_absolute_url(self):
    #    return reverse('show-need', args=(self.pk,))
