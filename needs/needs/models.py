from django.db import models
from django.urls import reverse


class NeedQuerySet(models.QuerySet):
    def create_from_activity(self, activity):
        for concept in activity.pattern.required_concepts.all():
            self.create(activity=activity, title=concept.title, description=concept.description)


class Need(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    creation_time = models.DateTimeField(auto_now_add=True)

    # either a need is created by a creator or it is created by an activity
    creator = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE, null=True)
    activity = models.ForeignKey(
            'activities.Activity', on_delete=models.CASCADE, null=True,
            related_name='required_needs')
    
    proposed_means = models.ManyToManyField('means.Means')

    objects = models.Manager.from_queryset(NeedQuerySet)()

    def get_absolute_url(self):
        return reverse('show-need', args=(self.pk,))
