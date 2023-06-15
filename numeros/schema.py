import graphene
from graphene_django import DjangoObjectType
from .models import Numero
from graphql import GraphQLError
from django.db.models import Q
from users.schema import UserType
from numeros.models import Numero, Vote


class NumeroType(DjangoObjectType):
    class Meta:
        model = Numero

class VoteType(DjangoObjectType):
    class Meta:
        model = Vote

class Query(graphene.ObjectType):
    numeros = graphene.List(NumeroType, search=graphene.String())
    votes = graphene.List(VoteType)
    
    def resolve_numeros(self, info, search=None, **kwargs):
        if search:
            filter = (
                Q(titulo__icontains=search) |
                Q(genero__icontains=search)
            )
            return Numero.objects.filter(filter)
        
        return Numero.objects.all()

    def resolve_votes(self, info, **kwargs):
        return Vote.objects.all()

#1
class CreateNumero(graphene.Mutation):
    id = graphene.Int()
    titulo = graphene.String()
    paginas = graphene.Int()
    autor = graphene.String()
    clasificacion = graphene.Int()
    pais = graphene.String()
    genero = graphene.String()
    capitulos = graphene.Int()
    serializacion = graphene.Int()
    precio = graphene.Int()
    posted_by = graphene.Field(UserType)

    #2
    class Arguments:
        id = graphene.Int()
        titulo = graphene.String()
        paginas = graphene.Int()
        autor = graphene.String()
        clasificacion = graphene.Int()
        pais = graphene.String()
        genero = graphene.String()
        capitulos = graphene.Int()
        serializacion = graphene.Int()
        precio = graphene.Int()

    #3
    def mutate(self, info, titulo, paginas, autor, clasificacion, pais, genero, capitulos, serializacion, precio ):
        
        user = info.context.user or None
        
        numero = Numero(titulo = titulo, paginas = paginas, autor = autor, clasificacion = clasificacion, pais = pais, genero = genero, capitulos = capitulos, serializacion = serializacion, precio = precio, posted_by=user,)
        numero.save()

        return CreateNumero(
            id=numero.id,
            titulo = numero.titulo,
            paginas =  numero.paginas,
            autor = numero.autor,
            clasificacion = numero.clasificacion,
            pais = numero.pais,
            genero = numero.genero,
            capitulos = numero.capitulos,
            serializacion = numero.serializacion,
            precio = numero.precio,
            posted_by=numero.posted_by
        )

class CreateVote(graphene.Mutation):
    user = graphene.Field(UserType)
    num = graphene.Field(NumeroType)

    class Arguments:
        num_id = graphene.Int()

    def mutate(self, info, num_id):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError('You must be logged to vote!')

        num = Numero.objects.filter(id=num_id).first()
        if not num:
            raise GraphQLError('Invalid Cap!')

        Vote.objects.create(
            user=user,
            num=num,
        )

        return CreateVote(user=user, num=num)

#4
class Mutation(graphene.ObjectType):
    create_Numero = CreateNumero.Field()
    create_link = CreateNumero.Field()
    create_vote = CreateVote.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)