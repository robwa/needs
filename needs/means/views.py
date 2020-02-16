from django.views.generic import CreateView

from needs.means.models import Means


class MeansCreateView(CreateView):
    model = Means
    fields = ('title', 'description')

    def get_success_url(self):
        return self.request.GET.get('next') or super().get_success_url()
