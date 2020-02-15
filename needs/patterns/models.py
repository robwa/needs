from django.db import models
from django.urls import reverse


class Pattern(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    required_concepts = models.ManyToManyField('concepts.Concept')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('show-pattern', args=(self.pk,))
