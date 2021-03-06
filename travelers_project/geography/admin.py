from django.contrib import admin

from geography.models import Region, City, TypeOfSights, Sight, SectionOfSights, SightPhoto


class SightPhotoInline(admin.TabularInline):
    model = SightPhoto


class SightAdmin(admin.ModelAdmin):
    inlines = [SightPhotoInline]
    list_display = ('id', 'title', 'city', 'text', 'coordinates', 'rating')
    list_display_links = ('title', 'city', 'text')
    search_fields = ['id', 'title']


class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'region', 'description', 'centre_coordinates', 'rating')
    list_display_links = ('title', 'region', 'description', )
    search_fields = ['id', 'title']


class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description',)
    list_display_links = ('title', 'description')
    search_fields = ['id', 'title']


class SightPhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'file', 'rating', 'sight')
    search_fields = ['id', 'title']


admin.site.register(Region, RegionAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(TypeOfSights)
admin.site.register(Sight, SightAdmin)
admin.site.register(SectionOfSights)
admin.site.register(SightPhoto, SightPhotoAdmin)
