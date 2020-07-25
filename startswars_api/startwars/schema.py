import graphene
from graphene import relay, ObjectType, Field, InputObjectType
from graphene_django.debug import DjangoDebug
from graphene_django.filter import DjangoFilterConnectionField

from .models import Planetas, Personajes, Peliculas

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

    """
    def res_pelicula(self, info, **kwargs):
        id = kwargs.get('idpl')

        if id is not None:
            return Pelicula.objects.get(pk=id)
        
        return None
    """


"""
    Construyendo las mutations
"""

class PlanetaInput(graphene.InputObjectType):
    idPla = graphene.ID()
    nombrePla = graphene.String()

class CreatePlaneta(graphene.Mutation):
    class Arguments:
        input = PlanetaInput(required=True)

    ok = graphene.Boolean()
    planeta = graphene.Field(PlanetasNode)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        planeta_instance = Planetas(nombrePla=input.nombrePla)
        planeta_instance.save()
        return CreatePlaneta(ok=ok, planeta=planeta_instance)

""" 
    Mutation personaje
"""
class PersonajeInput(graphene.InputObjectType):
    idpj = graphene.ID()
    nombrepj = graphene.String()

class CreatePersonaje(graphene.Mutation):

    class Arguments:
        input = PersonajeInput(required=True)

    ok = graphene.Boolean()
    personaje = graphene.Field(PersonajesNode)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        personaje_instance = Personajes(nombrepj=input.nombrepj)
        personaje_instance.save()
        return CreatePersonaje(ok=ok, personaje=personaje_instance)

""" 
    Mutation pelicula
"""
class PeliculaInput(graphene.InputObjectType):
    idpl = graphene.ID()
    nombrepl = graphene.String()
    productorespl = graphene.String()
    detallePl = graphene.String()
    directorpl = graphene.String()

class CreatePelicula(graphene.Mutation):

    class Arguments:
        input = PeliculaInput(required=True)

    ok = graphene.Boolean()
    pelicula = graphene.Field(PeliculasNode)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        pelicula_instance = Peliculas(
            nombrepl=input.nombrepl,
            productorespl=input.productorespl,
            detallePl=input.detallePl,
            directorpl=input.directorpl
            )
        pelicula_instance.save()
        return CreatePelicula(ok=ok, pelicula=pelicula_instance)

"""
    Register mutations
"""
class Mutation(ObjectType):
    create_planeta = CreatePlaneta.Field()
    create_personaje = CreatePersonaje.Field()
    create_pelicula = CreatePelicula.Field()
    