from django.contrib import admin
from django.urls import include, path

from needs.accounts.views import SignupView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup/', SignupView.as_view(), name='signup'),
]
