from django.views.generic import CreateView

from needs.concepts.models import Concept


class ConceptCreateView(CreateView):
    model = Concept
    fields = ('title', 'description')

    def get_success_url(self):
        return self.request.GET.get('next') or super().get_success_url()
