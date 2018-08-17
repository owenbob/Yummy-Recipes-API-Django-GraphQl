import json
from api.tests.base  import BaseTest

from api.fixtures.recipes_fixtures import(
    delete_query,
    delete_response,
    all_recipes,
    all_recipes_response,
    create_query,
    create_query_response,
    update_query,
    update_query_response
)

class RecipesTestCase(BaseTest):
    def test_all_recipes(self):
        query = self.client.post(
            '/yummyrecipesapi?query='+all_recipes,
            HTTP_AUTHORIZATION=self.test_token,
            content_type='application/json'
        )
        jresp = json.loads(query.content.decode())
        self.assertEquals(jresp,all_recipes_response)

    def test_create_recipe(self):
        query = self.client.post(
            '/yummyrecipesapi?query='+create_query,
            HTTP_AUTHORIZATION=self.test_token,
            content_type='application/json'
        )
        jresp = json.loads(query.content.decode())
        self.assertEquals(jresp,create_query_response)

    def test_update_and_delete_recipe(self):
        query = self.client.post(
            '/yummyrecipesapi?query='+update_query,
            HTTP_AUTHORIZATION=self.test_token,
            content_type='application/json'
        )
        jresp = json.loads(query.content.decode())
        self.assertEquals(jresp,update_query_response)

        query = self.client.post(
            '/yummyrecipesapi?query='+delete_query,
            HTTP_AUTHORIZATION=self.test_token,
            content_type='application/json'
        )
        jresp = json.loads(query.content.decode())
        self.assertEquals(jresp,delete_response)