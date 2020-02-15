from django.views.generic import CreateView

from needs.concepts.models import Concept


class ConceptCreateView(CreateView):
    model = Concept
    fields = ('title', 'description')
