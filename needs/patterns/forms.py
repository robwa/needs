from django import forms

from needs.concepts.models import Concept
from needs.patterns.models import Pattern


class PatternAddConceptForm(forms.ModelForm):
    class Meta:
        model = Pattern
        fields = []

    concept = forms.ModelChoiceField(queryset=Concept.objects.all())

    def save(self, commit=True):
        self.instance.required_concepts.add(self.cleaned_data['concept'])
        return super().save(commit)
