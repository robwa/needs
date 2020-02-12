from django.urls import path

from needs.needs.views import NeedCreateView, NeedDetailView, NeedListView

urlpatterns = [
    path('', NeedListView.as_view(), name='list-needs'),
    path('add/', NeedCreateView.as_view(), name='create-need'),
    path('<pk>/', NeedDetailView.as_view(), name='show-need'),
]
