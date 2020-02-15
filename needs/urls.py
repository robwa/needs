from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('accounts/', include('needs.accounts.urls')),
    path('activities/', include('needs.activities.urls')),
    path('admin/', admin.site.urls),
    path('concepts/', include('needs.concepts.urls')),
    path('needs/', include('needs.needs.urls')),
    path('patterns/', include('needs.patterns.urls')),
]
