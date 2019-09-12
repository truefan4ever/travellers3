from django.urls import path

from geography.api.views import RegionList
from geography.api.views import RegionDetail
from geography.api.views import CityList
from geography.api.views import CityDetail
from geography.api.views import SightList
from geography.api.views import SightDetail
from geography.api.views import SightPhotoList
from geography.api.views import SightPhotoDetail
from geography.api.views import SectionOfSightsList
from geography.api.views import SectionOfSightsDetail
from geography.api.views import TypeOfSightsList
from geography.api.views import TypeOfSightsDetail

urlpatterns = [
    path('regions/', RegionList.as_view()),
    path('region/<int:pk>/', RegionDetail.as_view()),
    path('cities/', CityList.as_view()),
    path('city/<int:pk>/', CityDetail.as_view()),
    path('sights/', SightList.as_view()),
    path('sight/<int:pk>/', SightDetail.as_view()),
    path('sightphotos/', SightPhotoList.as_view()),
    path('sightphoto/<int:pk>/', SightPhotoDetail.as_view()),
    path('sectionofsights/', SectionOfSightsList.as_view()),
    path('sectionofsights/<int:pk>/', SectionOfSightsDetail.as_view()),
    path('typeofsights/', TypeOfSightsList.as_view()),
    path('typeofsights/<int:pk>/', TypeOfSightsDetail.as_view()),
]
