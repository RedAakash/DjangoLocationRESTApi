from django.contrib import admin
from .models import (
    LocationData, Region, State, City, Country
)

admin.site.register(LocationData)
admin.site.register(Region)
admin.site.register(State)
admin.site.register(Country)
admin.site.register(City)
