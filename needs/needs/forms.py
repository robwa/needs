from django import forms

from needs.means.models import Means
from needs.needs.models import Need
from needs.patterns.models import Pattern


class NeedProposeMeansForm(forms.ModelForm):
    class Meta:
        model = Need
        fields = []

    means = forms.ModelChoiceField(queryset=Means.objects.all())

    def save(self, commit=True):
        self.instance.proposed_means.add(self.cleaned_data['means'])
        return super().save(commit)


class NeedProposePatternForm(forms.ModelForm):
    class Meta:
        model = Need
        fields = []

    pattern = forms.ModelChoiceField(queryset=Pattern.objects.all())

    def save(self, commit=True):
        self.instance.proposed_patterns.add(self.cleaned_data['pattern'])
        return super().save(commit)
