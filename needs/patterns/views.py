from django.views.generic import CreateView, DetailView, UpdateView

from needs.patterns.forms import PatternAddConceptForm
from needs.patterns.models import Pattern


class PatternAddConceptView(UpdateView):
    model = Pattern
    form_class = PatternAddConceptForm
    template_name = 'patterns/pattern_add_concept.html'


class PatternCreateView(CreateView):
    model = Pattern
    fields = ('title', 'description')


class PatternDetailView(DetailView):
    model = Pattern
