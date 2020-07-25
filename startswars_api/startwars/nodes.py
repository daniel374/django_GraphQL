from graphene import relay
from graphene_django import DjangoObjectType

from .models import Peliculas, Personajes, Planetas, Persopelis, Planetaspelis

class PeliculasNode(DjangoObjectType):
    class Meta:
        model = Peliculas
        interfaces = (relay.Node, )
        filter_fields = {
            'idpl': ['exact', 'gt', 'gte', 'lt', 'lte'],
            'nombrepl': ['exact', 'icontains', 'istartswith'],
            'directorpl': ['exact', 'icontains', 'istartswith']
        }

class PlanetasNode(DjangoObjectType):
    class Meta:
        model = Planetas
        interfaces = (relay.Node, )
        filter_fields = {
            'idPla': ['exact', 'gt', 'gte', 'lt', 'lte'],
            'nombrePla': ['exact', 'icontains', 'istartswith']
        }

class PersonajesNode(DjangoObjectType):
    class Meta:
        model = Personajes
        interfaces = (relay.Node, )
        filter_fields = {
            'idpj': ['exact', 'gt', 'gte', 'lt', 'lte'],
            'nombrepj': ['exact', 'icontains', 'istartswith']
        }

class PersopelisNode(DjangoObjectType):
    class Meta:
        model = Persopelis
        interfaces = (relay.Node, )
        filter_fields = {
            'idpeli': ['exact', 'gt', 'gte', 'lt', 'lte'],
            'idper': ['exact', 'gt', 'gte', 'lt', 'lte']
        }

class PlanetaspelisNode(DjangoObjectType):
    class Meta:
        model = Planetaspelis
        interfaces = (relay.Node, )
        filter_fields = {
            'idpeli': ['exact', 'gt', 'gte', 'lt', 'lte'],
            'idplaneta': ['exact', 'gt', 'gte', 'lt', 'lte']
        }