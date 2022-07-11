from django.contrib import admin

from .models import Links


@admin.register(Links)
class AdminLinks(admin.ModelAdmin):
    list_display = ('user', 'input_link', 'output_link', 'date_create_link')

