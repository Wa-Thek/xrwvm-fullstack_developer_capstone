# from django.contrib import admin
# from .models import CarMake, CarModel

# # Define an inline class for CarModel to be displayed within CarMake admin page
# class CarModelInline(admin.TabularInline):
#     model = CarModel
#     extra = 1  # Number of empty CarModel forms to display

# # Customize the CarMake admin interface
# class CarMakeAdmin(admin.ModelAdmin):
#     inlines = [CarModelInline]  # Show CarModels as inlines
#     list_display = ('name', 'description')  # Columns to display in list view

# # Register models with the admin site
# admin.site.register(CarMake, CarMakeAdmin)
# admin.site.register(CarModel)

# CarModelInline class

# CarModelAdmin class

# CarMakeAdmin class with CarModelInline

# Register models here

from django.contrib import admin
from .models import CarMake, CarModel

# Registering models with their respective admins
admin.site.register(CarMake)
admin.site.register(CarModel)