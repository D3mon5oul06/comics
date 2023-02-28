import graphene
from graphene_django import DjangoObjectType

from .models import Numero


class NumeroType(DjangoObjectType):
    class Meta:
        model = Numero


class Query(graphene.ObjectType):
    Numero = graphene.List(NumeroType)

    def resolve_Numero(self, info, **kwargs):
        return Numero.objects.all()