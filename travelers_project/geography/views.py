from django.views.generic.detail import DetailView
from django.views.generic.list import MultipleObjectMixin, ListView

from sorl.thumbnail import get_thumbnail

from travelers_project.settings import DEFAULT_PHOTO_PATH

from geography.models import City, Sight, Region, TypeOfSights, SightPhoto

mock_text = """There are many variations of passages of Lorem Ipsum available,
    but the majority have suffered alteration in some form, by injected humour, or randomised word.
    Richard McClintock."""


class RegionList(ListView):
    model = Region
    template_name = 'geography/regions.html'
    context_object_name = 'region_list'
    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        context = super(RegionList, self).get_context_data(*args, **kwargs)
        context['mock_text'] = mock_text

        try:
            file = open(DEFAULT_PHOTO_PATH)
            default_image = get_thumbnail(file, 'x100', crop='center')
            context['default_image'] = default_image
        except FileExistsError:
            pass

        return context


class RegionDetail(DetailView, MultipleObjectMixin):
    model = Region
    template_name = 'geography/region_detail.html'
    context_object_name = 'region_detail'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        object_list = City.objects.filter(region=self.get_object())
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['mock_text'] = mock_text

        try:
            file = open(DEFAULT_PHOTO_PATH)
            default_image = get_thumbnail(file, 'x150', crop='center')
            context['default_image'] = default_image
        except FileExistsError:
            pass

        return context


class CityList(ListView):
    model = City
    template_name = 'geography/city_list.html'
    context_object_name = 'city_list'
    paginate_by = 12

    def get_context_data(self, *args, **kwargs):
        context = super(CityList, self).get_context_data(*args, **kwargs)
        context['mock_text'] = mock_text

        try:
            file = open(DEFAULT_PHOTO_PATH)
            default_image = get_thumbnail(file, 'x150', crop='center')
            context['default_image'] = default_image
        except FileExistsError:
            pass

        return context


class CityDetail(DetailView):
    model = City
    template_name = 'geography/city_detail.html'
    context_object_name = 'city_detail'


class SightList(ListView):
    model = Sight
    template_name = 'geography/sight_list.html'
    context_object_name = 'sight_list'


class SightDetail(DetailView):
    model = Sight
    template_name = 'geography/sight_detail.html'
    context_object_name = 'sight_detail'
