from django.db import models
from django.urls import reverse


class NeedQuerySet(models.QuerySet):
    def create_from_pattern(self, pattern):
        for concept in pattern.required_concepts.all():
            self.create(title=concept.title, description=concept.description)


class Need(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    creation_time = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE, null=True)
    proposed_means = models.ManyToManyField('means.Means')
    proposed_patterns = models.ManyToManyField('patterns.Pattern')

    objects = models.Manager.from_queryset(NeedQuerySet)()

    def get_absolute_url(self):
        return reverse('show-need', args=(self.pk,))
