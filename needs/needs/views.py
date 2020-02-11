from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView

from needs.needs.models import Need


class NeedCreateView(LoginRequiredMixin, CreateView):
    model = Need
    fields = ('title', 'description')
    success_url = '/needs'


class NeedListView(ListView):
    model = Need
