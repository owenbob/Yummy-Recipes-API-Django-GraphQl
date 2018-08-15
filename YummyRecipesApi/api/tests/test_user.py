from api.tests.base import BaseTest

from api.fixtures.user_fixtures import (
    create_user_query,
    create_user_query_response,
    get_all_users_query,
    get_all_users_response
)

class UserTestCase(BaseTest):
    def test_create_user(self):
        query = self.client.execute(create_user_query)
        self.assertEquals(query,create_user_query_response)

    def test_get_all_users(self):
        query =  self.client.execute(get_all_users_query)
        self.assertEquals(query,get_all_users_query)


    