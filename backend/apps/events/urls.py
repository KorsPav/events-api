from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('', views.EventViewSet, basename='events')

urlpatterns = []

urlpatterns += router.urls
