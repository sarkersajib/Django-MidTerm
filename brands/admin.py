from django.contrib import admin

# Register your models here.
from . import models
# Register your models here.
#admin.site.register(models.Category)
class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ['name', 'slug']

admin.site.register(models.Brand,BrandAdmin)