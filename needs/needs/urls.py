from django.conf.urls import url

from needs.needs.views import NeedCreateView, NeedListView

urlpatterns = [
    url(r'^$', NeedListView.as_view(), name='list-needs'),
    url(r'^add/$', NeedCreateView.as_view(), name='create-need'),
]
