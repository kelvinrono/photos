from django.contrib import admin
from .models import Gallery, Location, Category

admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Gallery)
