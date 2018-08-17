from django.test import TestCase
from graphene.test import Client
from django.test import Client as DjangoTestClient
from django.contrib.auth import get_user_model
from api.fixtures.user_fixtures import (
    login_user_query
)

from YummyRecipesApi.schema import schema
from api.models import (
    Categories,
    Recipes
    )


User = get_user_model()



class BaseTest(TestCase):
    

    def setUp(self):
        self.test_client = Client(schema)
        self.client = DjangoTestClient()
        self.maxDiff = None

        test_user = User(
            username="Jackson",
            email="jacks@gmail.com"
        )
        test_user.set_password(123)
        test_user.save()

        cat = Categories(
            category_title="Breakfast",
            category_description="First meal of the day",
            user=User.objects.get(
                username="Jackson",
                email="jacks@gmail.com"
            )
        )
        cat.save()

        rec = Recipes(
            category=Categories.objects.get(
            category_title="Breakfast",
            category_description="First meal of the day"
        ),
        recipe_title="Rolex",
        recipe_description="Eggs"
        )
        rec.save()

        

        self.login_query = login_user_query
        test_login =  self.test_client.execute(self.login_query)
        self.test_token = ("JWT {}".format(test_login["data"]["loginUser"]["token"]))
