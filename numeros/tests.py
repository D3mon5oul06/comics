from graphene_django.utils.testing import GraphQLTestCase
from numeros.models import Numero
from mixer.backend.django import mixer
import graphene
import json

# Create your tests here.
from numeros.schema import schema
from numeros.models import Numero

LINKS_QUERY = '''
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
class NumeroTestCase(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema
    def setUp(self):
        self.numero1 = mixer.blend(Numero)
        self.numero2= mixer.blend(Numero)
        
    def test_numeros_query(self):
        response = self.query(
            LINKS_QUERY
            )
        
        content = json.loads(response.content)
            #print (content)
        self.assertResponseNoErrors(response)
        print ("query numeros results")
        print (content)
        assert len(content['data']['numeros']) == 2
