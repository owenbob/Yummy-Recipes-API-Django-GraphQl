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
        query = self.client.execute(all_recipes)
        self.assertEquals(query,all_recipes_response)

    def test_create_recipe(self):
        query = self.client.execute(create_query)
        self.assertEquals(query,create_query_response)

    def test_update_and_delete_recipe(self):
        query = self.client.execute(update_query)
        self.assertEquals(query,update_query_response)

        query = self.client.execute(delete_query)
        self.assertEquals(query,delete_response)