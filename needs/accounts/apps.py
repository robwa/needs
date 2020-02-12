from django.apps import AppConfig


class AccountConfig(AppConfig):
    name = 'needs.accounts'

    def ready(self):
        from . import signals
