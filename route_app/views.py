from django.shortcuts import render
from .models import Bus, Route, BusRoute
from .tables import BusTable, BusRouteTable, RouteTable, RouteBusTable
from django.db.models import Count, QuerySet


# Create your views here.
def index(request):
    return render(request, 'route_app/index.html')


def get_buses(request):
    table = BusTable(Bus.objects.annotate(number_of_routes=Count('routes')))
    context = {
        'table': table
    }
    return render(request, 'route_app/table.html', context)



def get_bus_routes(request, id):
    bus = Bus.objects.get(pk=id)
    bus_routes = BusRoute.objects.filter(bus=bus)
    table = BusRouteTable(bus_routes)
    context = {
        'table' : table
    }
    return render(request, 'route_app/table.html', context)


def get_routes(request):
    routes = Route.objects.annotate(numbers_of_buses=Count('bus'))
    table = RouteTable(routes)
    context = {
        'table' : table
    }
    return render(request, 'route_app/table.html', context)

def get_route_buses(request, id):
    route = Route.objects.get(pk=id)
    bus_routes = BusRoute.objects.filter(route=route)
    table = RouteBusTable(bus_routes)
    context = {
        'table' : table
    }
    return render(request, 'route_app/table.html', context)
