from django.test import TestCase
from YummyRecipesApi.schema import schema

from graphene.test import Client
from api.models import Categories



class BaseTest(TestCase):
    def setUp(self):
        self.client = Client(schema)
        self.maxDiff = None

        cat = Categories(
            category_title="Breakfast",
            category_description="First meal of the day"
        )
        cat.save()

            