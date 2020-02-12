from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView

from needs.needs.models import Need


class NeedCreateView(LoginRequiredMixin, CreateView):
    model = Need
    fields = ('title', 'description')
    success_url = '/needs'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = Need(creator=self.request.user.profile)
        return kwargs


class NeedDetailView(DetailView):
    model = Need


class NeedListView(ListView):
    model = Need
