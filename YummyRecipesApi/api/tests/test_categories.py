import json
from api.tests.base import BaseTest
from api.fixtures.categories_fixtures import (
    create_query,
    create_query_response,
    update_query,
    update_query_response,
    delete_query,
    delete_query_response,
    all_categories,
    all_categories_response
)

class CategoryTestCase(BaseTest):
    def test_all_categories(self):
        query = self.client.post(
            '/yummyrecipesapi?query='+all_categories,
            HTTP_AUTHORIZATION=self.test_token,
            content_type='application/json'
        )
        jresp = json.loads(query.content.decode())
        
        self.assertEquals(jresp,all_categories_response)

    def test_creation(self):
        query = self.client.post(
            '/yummyrecipesapi?query='+create_query,
            HTTP_AUTHORIZATION=self.test_token,
            content_type='application/json'
        )
        jresp = json.loads(query.content.decode())
        
        self.assertEquals(jresp,create_query_response)

    # def test_update_and_delete(self):
    #     query = self.client.post(
    #         '/yummyrecipesapi?query='+update_query,
    #         HTTP_AUTHORIZATION=self.test_token,
    #         content_type='application/json'
    #     )
    #     jresp = json.loads(query.content.decode())
    #     self.assertEquals(jresp,update_query_response)

    #     query = self.client.post(
    #         '/yummyrecipesapi?query='+delete_query,
    #         HTTP_AUTHORIZATION=self.test_token,
    #         content_type='application/json'
    #     )
    #     jresp = json.loads(query.content.decode())
    #     self.assertEquals(jresp,delete_query_response)
