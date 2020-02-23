from django.urls import path

from needs.patterns.views import PatternAddConceptView, PatternCreateView, PatternDetailView
from needs.patterns.views import PatternListView

urlpatterns = [
    path('', PatternListView.as_view(), name='list-patterns'),
    path('add/', PatternCreateView.as_view(), name='create-pattern'),
    path('<pk>/', PatternDetailView.as_view(), name='show-pattern'),
    path('<pk>/concepts/add/', PatternAddConceptView.as_view(), name='add-concept-to-pattern'),
]
