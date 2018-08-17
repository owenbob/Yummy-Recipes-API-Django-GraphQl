from api.tests.base import BaseTest



class LoginUser(BaseTest):
    def test_login_user(self):
        query = self.test_client.execute(self.login_query)
        assert "data" in query
        assert "loginUser" in query["data"]
        assert "token" in query["data"]["loginUser"]
        