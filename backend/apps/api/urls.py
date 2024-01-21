from django.urls import path, include

app_name = 'api'
urlpatterns = [
    path('users/', include('apps.users.urls')),
    path('events/', include('apps.events.urls')),
]
