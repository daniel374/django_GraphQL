from graphene import relay
from graphene_django import DjangoObjecType

from .models import Peliculas, Personajes, Planetas, Persopelis, Planetaspelis

class PeliculasNode(DjangoObjecType):
    class Meta:
        model = Peliculas
        interfaces = (relay.Node, )
        filter_fields = {
            'idpl': ['exact', 'gt', 'gte', 'lt', 'lte'],
            'nombrepl': ['exact', 'icontains', 'istartswith'],
            'directorpl': ['exact', 'icontains', 'istartswith']
        }

class PlanetasNode(DjangoObjecType):
    class Meta:
        model = Planetas
        interfaces = (relay.Node, )
        filter_fields = {
            'idPla': ['exact', 'gt', 'gte', 'lt', 'lte'],
            'nombrePla': ['exact', 'icontains', 'istartswith']
        }

class PersonajesNode(DjangoObjecType):
    class Meta:
        model = Personajes
        interfaces = (relay.Node, )
        filter_fields = {
            'idpj': ['exact', 'gt', 'gte', 'lt', 'lte'],
            'nombrepj': ['exact', 'icontains', 'istartswith']
        }

class PersopelisNode(DjangoObjecType):
    class Meta:
        model = Persopelis
        interfaces = (relay.Node, )
        filter_fields = {
            'idpeli': ['exact', 'gt', 'gte', 'lt', 'lte'],
            'idper': ['exact', 'gt', 'gte', 'lt', 'lte']
        }

class PlanetaspelisNode(DjangoObjecType):
    class Meta:
        model = Planetaspelis
        interfaces = (relay.Node, )
        filter_fields = {
            'idpeli': ['exact', 'gt', 'gte', 'lt', 'lte'],
            'idplaneta': ['exact', 'gt', 'gte', 'lt', 'lte']
        }