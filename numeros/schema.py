import graphene
from graphene_django import DjangoObjectType

from .models import Numero


class NumeroType(DjangoObjectType):
    class Meta:
        model = Numero


class Query(graphene.ObjectType):
    numeros = graphene.List(NumeroType)

    def resolve_numeros(self, info, **kwargs):
        return Numero.objects.all()

# ...code
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
        numero = Numero(titulo = titulo, paginas = paginas, autor = autor, clasificacion = clasificacion, pais = pais, genero = genero, capitulos = capitulos, serializacion = serializacion, precio = precio)
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
        )


#4
class Mutation(graphene.ObjectType):
    create_Numero = CreateNumero.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)