import graphene
from graphene_django.debug import DjangoDebug

import startwars.schema

class Query (startwars.schema.Query, graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name='__debug')

class Mutation (startwars.schema.Mutation, graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name='__debug')

schema = graphene.Schema(
    query=Query,
    mutation=Mutation
)