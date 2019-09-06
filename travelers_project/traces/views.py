from django.views.generic import DetailView
from django.views.generic import ListView

from .models import RouteByCities
from .models import RouteBySights


class RouteByCitiesList(ListView):
    model = RouteByCities
    context_object_name = 'route_cities_list'
    template_name = 'traсes/route_cities_list.html'


class RouteByCitiesDetail(DetailView):
    model = RouteByCities
    context_object_name = 'route_cities_detail'
    template_name = 'traсes/route_cities_detail.html'


class RouteBySightsList(ListView):
    model = RouteBySights
    context_object_name = 'route_sights_list'
    template_name = 'traсes/route_sights_list.html'


class RouteBySightsDetail(DetailView):
    model = RouteBySights
    context_object_name = 'route_sights_detail'
    template_name = 'traсes/route_sights_detail.html'

