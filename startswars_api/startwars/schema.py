from graphene import relay, ObjectType, Field
from graphene_django.debug import DjangoDebug
from graphene_django.filter import DjangoFilterConnectionField

from .nodes import PersonajesNode
class Query(ObjectType):
    personaje = relay.Node.Field(PersonajesNode)
    personajes = DjangoFilterConnectionField(PersonajesNode)
    debug = Field(DjangoDebug, name='__debug')

class Mutation(ObjectType):
    debug = Field(DjangoDebug, name='__debug')

schema = Schema(
    query=Query,
    mutation=Mutation
)