from rest_framework.serializers import ModelSerializer
from route_app.models import Route, Bus, BusRoute

class RouteSerializer(ModelSerializer):
    class Meta:
        model = Route
        fields = '__all__'

class BusSerializer(ModelSerializer):
    class Meta:
        model = Bus
        fields = '__all__'

class BusRouteSerializer(ModelSerializer):
    class Meta:
        model = BusRoute
        fields = '__all__'