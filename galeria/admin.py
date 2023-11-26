from django.contrib import admin

from galeria.models import Fotografia

class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "nome", "categoria", "legenda", "data_fotografia", "publicada")
    list_display_links = ("id","nome", "categoria", "legenda")
    search_fields = ("nome",)
    list_filter = ("categoria",)
    list_editable = ("publicada",)


admin.site.register(Fotografia, ListandoFotografias)
