from rest_framework.routers import DefaultRouter
from .views import PublicationViewSet


default_router = DefaultRouter()

default_router.register('publications', PublicationViewSet, basename='publications')

urlpatterns = default_router.urls
