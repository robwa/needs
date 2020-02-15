from django.urls import path

from needs.concepts.views import ConceptCreateView

urlpatterns = [
    path('add/', ConceptCreateView.as_view(), name='create-concept'),
]
