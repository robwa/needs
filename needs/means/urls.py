from django.urls import path

from needs.means.views import MeansCreateView

urlpatterns = [
    path('add/', MeansCreateView.as_view(), name='create-means'),
]
