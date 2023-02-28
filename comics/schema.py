import graphene

import numeros.schema


class Query(numeros.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)