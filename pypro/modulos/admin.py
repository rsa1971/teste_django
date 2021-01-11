from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin
from pypro.modulos.models import Modulo, Aula


@admin.register(Modulo)
class ModuloAdmin(OrderedModelAdmin):
    list_display = ('titulo', 'publico', 'move_up_down_links')
    prepolated_fields = {'slug': ('titulo',)}


@admin.register(Aula)
class AulaAdmin(OrderedModelAdmin):
    list_display = ('titulo', 'modulo', 'move_up_down_links')
    list_filter = ('modulo',)
    prepolated_fields = {'slug': ('titulo',)}
