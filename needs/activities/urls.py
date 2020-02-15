from django.urls import path

from needs.activities.views import ActivityCreateView, ActivityDetailView, ActivityListView

urlpatterns = [
    path('', ActivityListView.as_view(), name='list-activities'),
    path('<pk>/', ActivityDetailView.as_view(), name='show-activity'),
    path('<need_pk>/activities/add/', ActivityCreateView.as_view(), name='create-activity'),
]
