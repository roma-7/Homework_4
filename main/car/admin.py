from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import *

admin.site.register(Car)


class CarAdmin(TranslationAdmin):
    list_display = ("car_name",)


admin.site.register(CarModel)
admin.site.register(Marka)
