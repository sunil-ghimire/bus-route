from rest_framework.routers import DefaultRouter
from .views import *
from django.urls import path, include

router = DefaultRouter()
router.register('buses', BusViewSet, basename='buses')
router.register('routes', RouteViewSet, basename='routes')
router.register('bus_routes', BusRouteViewSet, basename='bus_routes')

urlpatterns = [
    path('', include(router.urls)),
]
