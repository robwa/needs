from django import forms

from needs.means.models import Means
from needs.needs.models import Need


class NeedProposeMeansForm(forms.ModelForm):
    class Meta:
        model = Need
        fields = []

    means = forms.ModelChoiceField(queryset=Means.objects.all())

    def save(self, commit=True):
        self.instance.proposed_means.add(self.cleaned_data['means'])
        return super().save(commit)
