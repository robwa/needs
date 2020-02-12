from django.contrib.auth.signals import user_logged_in

from django.dispatch import receiver

from needs.accounts.models import Profile


@receiver(user_logged_in)
def check_profile(sender, request, user, **kwargs):
    Profile.objects.get_or_create(user=user)
