from django.contrib import admin
from .models import Refugio

class RefugioAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_registro',)
    

admin.site.register(Refugio, RefugioAdmin)

