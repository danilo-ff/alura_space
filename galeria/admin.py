from django.contrib import admin

from galeria.models import Fotografia

class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "nome", "categoria", "usuarios", "data_fotografia", "publicada")
    list_display_links = ("nome", "categoria", "usuarios")
    search_fields = ("nome",)
    list_filter = ("categoria", "usuarios")
    list_editable = ("publicada",)


admin.site.register(Fotografia, ListandoFotografias)
