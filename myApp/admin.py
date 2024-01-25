from django.contrib import admin
from myApp.models import Beer

# Register your models here.
# class BeerAdmin(admin.ModelAdmin):

#     list_display = ['name', 'teste', 'color', 'price']

# admin.site.register(Beer, BeerAdmin)

admin.site.register(Beer)
