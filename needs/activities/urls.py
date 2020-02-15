from django.urls import path

from needs.activities.views import ActivityCreateView, ActivityDetailView, ActivityListView
from needs.activities.views import ActivityParticipateView

urlpatterns = [
    path('', ActivityListView.as_view(), name='list-activities'),
    path('<pk>/', ActivityDetailView.as_view(), name='show-activity'),
    path('<pk>/participants/add/', ActivityParticipateView.as_view(), name='participate-in-activity'),
    # FIXME: move this to needs?
    path('<need_pk>/activities/add/', ActivityCreateView.as_view(), name='create-activity'),
]
