from graphene_django.utils.testing import GraphQLTestCase
from numeros.models import Numero
from mixer.backend.django import mixer
import graphene
import json

# Create your tests here.
from numeros.schema import schema
from numeros.models import Numero

NUMEROS_QUERY = '''
{
    numeros {
    id
    titulo
    paginas
    autor
    clasificacion
    pais
    genero
    capitulos
    serializacion
    precio
    }
}
'''
CREATE_NUMERO_MUTATION = '''
mutation createNumeroMutation($titulo: String, $paginas: String, $paginas: Int, $autor: String, $clasificacion: Int, $pais: String, $genero: String, $capitulos: Int, $serializacion: Int, $precio: Int ){
    createNumero(titulo: $titulo, paginas: $paginas, autor: $autor,  clasificacion: $clasificacion,  pais: $pais,  genero: $genero,  capitulos: $capitulos,  serializacion: $serializacion,  precio: $precio){
    titulo
    paginas
    autor
    clasificacion
    pais
    genero
    capitulos
    serializacion
    precio
    }
}
'''
class NumeroTestCase(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema
    def setUp(self):
        self.numero1 = mixer.blend(Numero)
        self.numero2= mixer.blend(Numero)
        
    def test_numeros_query(self):
        response = self.query(
            NUMEROS_QUERY
            )
        
        content = json.loads(response.content)
            #print (content)
        self.assertResponseNoErrors(response)
        print ("query numeros results")
        print (content)
        assert len(content['data']['numeros']) == 2

    def CREATE_NUMERO_MUTATION(self):

        response = self.query(
            CREATE_NUMERO_MUTATION,
            variables={'titulo': 'knight', 'paginas': 12, 'autor': 'john', 'clasificacion': 18, 'pais': 'Estados Unidos', 'genero': 'accion', 'capitulos': 12, 'serializacion': 124543245, 'precio': 12}
        )
        print('mutation ')
        print(response)
        content = json.loads(response.content)
        print(content)
        self.assertResponseNoErrors(response)
        self.assertDictEqual({"createNumero": {'titulo': 'knight', 'paginas': 12, 'autor': 'john', 'clasificacion': 18, 'pais': 'Estados Unidos', 'genero': 'accion', 'capitulos': 12, 'serializacion': 124543245, 'precio': 12}}, content['data'])
