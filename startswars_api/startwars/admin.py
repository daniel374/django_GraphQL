from django.contrib import admin

# Register your models here.
from startwars.models import Peliculas, Personajes, Persopelis, Planetas, Planetaspelis

@admin.register(Peliculas)
class PeliculasAdmin(admin.ModelAdmin):
    list_display = ('idpl',)
    ordering = ('idpl',)
    

@admin.register(Personajes)
class PersonajesAdmin(admin.ModelAdmin):
    list_display = ('idpj', 'nombrepj')
    ordering = ('idpj',)
    #raw_id_fields = ('evolve_from', 'type_1', 'type_2', )

@admin.register(Planetas)
class PlanetasAdmin(admin.ModelAdmin):
    list_display = ('idPla', 'nombrePla')
    ordering = ('idPla',)

@admin.register(Persopelis)
class PersopelisAdmin(admin.ModelAdmin):
    pass


@admin.register(Planetaspelis)
class PlanetaspelisAdmin(admin.ModelAdmin):
    pass