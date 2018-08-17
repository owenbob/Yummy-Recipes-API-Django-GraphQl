import json
from api.tests.base import BaseTest

from api.fixtures.user_fixtures import (
    create_user_query,
    create_user_query_response,
    get_all_users_query ,
    get_all_users_response
)

class UserTestCase(BaseTest):

    def test_get_all_users(self):
        query = self.client.post(
            '/yummyrecipesapi?query='+get_all_users_query,
            HTTP_AUTHORIZATION=self.test_token,
            content_type='application/json'
        )
        jresp = json.loads(query.content.decode())
        self.assertEquals(jresp,get_all_users_response) 

    def test_create_user(self):
        query = self.test_client.execute(create_user_query)
        self.assertEquals(query,create_user_query_response)
