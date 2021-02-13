from django.contrib import admin
from .models import Services

class ServicesAdmin(admin.ModelAdmin):
    readonly_fields=('Created', 'Updated')

admin.site.register(Services, ServicesAdmin)