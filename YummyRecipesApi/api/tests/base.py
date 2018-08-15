from django.test import TestCase
from graphene.test import Client
from django.contrib.auth import get_user_model

from YummyRecipesApi.schema import schema
from api.models import (
    Categories,
    Recipes
    )


User = get_user_model()



class BaseTest(TestCase):
    def setUp(self):
        self.client = Client(schema)
        self.maxDiff = None

        cat = Categories(
            category_title="Breakfast",
            category_description="First meal of the day"
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

        test_user = User(
            username="Jackson",
            email="jacks@gmail.com"
        )
        test_user.set_password(123)
        test_user.save()
        
