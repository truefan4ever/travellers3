import graphene
from graphene_django.types import DjangoObjectType
from django.db.models import Max

from geography.models import City, Region, Sight


class CityType(DjangoObjectType):
    class Meta:
        model = City


class RegionType(DjangoObjectType):
    class Meta:
        model = Region


class SightType(DjangoObjectType):
    class Meta:
        model = Sight


class Query(graphene.ObjectType):
    all_cities = graphene.List(CityType)
    all_regions = graphene.List(RegionType)
    region = graphene.Field(RegionType, title=graphene.String())
    best_cities = graphene.List(CityType, id=graphene.Int())
    best_sight_in_region = graphene.List(SightType, id=graphene.Int())


    def resolve_all_cities(self, info, **kwargs):
        return City.objects.all()

    def resolve_region(self, info, **kwargs):
        title = kwargs.get('title')

        if title:
            return Region.objects.get(title=title)
        return None

    def resolve_best_cities(self, info, **kwargs):
        region_id = kwargs.get('id')
        cities = City.objects.filter(region=region_id)
        city_max = cities.aggregate(Max('rating'))
        filtered_cities = cities.filter(rating=city_max['rating__max'])

        if region_id:
            return filtered_cities
        return None

    def resolve_all_regions(self, info, **kwargs):
        return Region.objects.all()

    def resolve_best_sight_in_region(self, info, **kwargs):
        region_id = kwargs.get('id')
        sights = Sight.objects.filter(city__in=City.objects.filter(region=region_id))
        sight_max = sights.aggregate(Max('rating'))
        filtered_sights = sights.filter(rating=sight_max['rating__max'])

        if region_id:
            return filtered_sights
        return None
