from django.contrib import admin
from registrycontrol.models import *

class ListImobiliaria(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'phone',)
    list_per_page = 10

class ListImovel(admin.ModelAdmin):
    list_display = ('id', 'imobiliaria', 'address', 'value', 'sold')
    list_display_links = ('id', 'imobiliaria', 'address')
    search_fields = ('address', 'value',)
    list_editable = ('sold',)
    list_per_page = 10

admin.site.register(Imobiliaria, ListImobiliaria)
admin.site.register(Imovel, ListImovel)