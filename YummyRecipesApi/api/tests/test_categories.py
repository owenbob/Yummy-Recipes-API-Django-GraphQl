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
        query = self.client.execute(all_categories)
        self.assertEquals(query,all_categories_response)

    def test_creation(self):
        query = self.client.execute(create_query)
        self.assertEquals(query,create_query_response)

    def test_update_and_delete(self):
        query = self.client.execute(update_query)
        self.assertEquals(query,update_query_response)

        query = self.client.execute(delete_query)
        self.assertEquals(query,delete_query_response)

    




       

