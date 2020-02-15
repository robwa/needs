from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from needs.needs.forms import NeedProposeMeansForm, NeedProposePatternForm
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


class NeedProposeMeansView(UpdateView):
    model = Need
    form_class = NeedProposeMeansForm
    template_name = 'needs/need_propose_means.html'


class NeedProposePatternView(UpdateView):
    model = Need
    form_class = NeedProposePatternForm
    template_name = 'needs/need_propose_pattern.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        Need.objects.create_from_pattern(form.cleaned_data['pattern'])
        return response
