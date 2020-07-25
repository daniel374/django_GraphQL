from graphene import relay, ObjectType, Field
from graphene_django.debug import DjangoDebug
from graphene_django.filter import DjangoFilterConnectionField

from .nodes import PeliculasNode, PlanetasNode, PersonajesNode, PersopelisNode, PlanetaspelisNode


class Query(ObjectType):
    pelicula = relay.Node.Field(PeliculasNode)
    peliculas = DjangoFilterConnectionField(PeliculasNode)

    planeta = relay.Node.Field(PlanetasNode)
    planetas = DjangoFilterConnectionField(PlanetasNode)

    personaje = relay.Node.Field(PersonajesNode)
    personajes = DjangoFilterConnectionField(PersonajesNode)

    persopeli = relay.Node.Field(PersopelisNode)
    persopelis = DjangoFilterConnectionField(PersopelisNode)

    planepeli = relay.Node.Field(PlanetaspelisNode)
    planepelis = DjangoFilterConnectionField(PlanetaspelisNode)

class Mutation(ObjectType):
    pass