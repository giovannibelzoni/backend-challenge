from django.urls import path, include


urlpatterns = [
    path(r'api/', include('backend_challenge.pulse.urls')),
]
