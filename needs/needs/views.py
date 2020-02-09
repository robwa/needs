from django.views.generic import ListView

from needs.needs.models import Need


class NeedListView(ListView):
    model = Need
