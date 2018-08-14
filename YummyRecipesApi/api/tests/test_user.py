from api.tests.base import BaseTest

from api.fixtures.user_fixtures import (
    create_user_query,
    create_user_query_response
)

class UserTestCase(BaseTest):
    def test_create_user(self):
        query = self.client.execute(create_user_query)
        self.assertEquals(query,create_user_query_response)