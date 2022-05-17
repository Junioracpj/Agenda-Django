from django.contrib import admin
from core.models import Evento


# necessario importacao

# Register your models here.

class EventoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'data_evento', 'dat_criacao')
    list_filter = ('usuario', 'data_evento',)


admin.site.register(Evento, EventoAdmin)
# importa a classe feita no arquivo models
