from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView

from needs.activities.models import Activity
from needs.needs.models import Need


class ActivityListView(ListView):
    model = Activity


class ActivityCreateView(CreateView):
    model = Activity
    fields = ('pattern',)

    def form_valid(self, form):
        response = super().form_valid(form)
        Need.objects.create_from_activity(self.object)
        return response

    def get_form_kwargs(self):
        self.need = Need.objects.get(pk=self.kwargs.get('need_pk'))
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = Activity(result_need=self.need)
        return kwargs

    def get_success_url(self):
        return reverse('show-need', args=(self.need.pk,))


class ActivityDetailView(DetailView):
    model = Activity
