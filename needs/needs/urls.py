from django.conf.urls import url

from needs.needs.views import NeedListView

urlpatterns = [
    url(r'^$', NeedListView.as_view()),
]
