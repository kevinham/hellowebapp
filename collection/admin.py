from django.contrib import admin

# Register your models here.
from collection.models import Laptops

# set up automated slug creation
class LaptopsAdmin(admin.ModelAdmin):
    model = Laptops
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug':('name',)}


# and register it
admin.site.register(Laptops, LaptopsAdmin)
