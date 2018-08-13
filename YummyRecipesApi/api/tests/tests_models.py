from django.test import TestCase
from api.models import (
    Categories,
    Recipes
)

# Create your tests here.

class TestModels(TestCase):
    def test_string_representation(self):
        category = Categories(category_title="My Recipe")
        recipe = Recipes(recipe_title="My Recipe")

        self.assertEqual(str(category), category.category_title)
        self.assertEqual(str(recipe), recipe.recipe_title)

    def test_all_models(self):
        t = Categories(
            category_title="My category",
            category_description="My category description"
        )

        t.save()

        r = Recipes(
            recipe_title="My recipe",
            recipe_description="My recipe description",
            category=Categories.objects.get(
                category_title="My category",
                category_description="My category description"
                )
        )
        
        r.save()
 
        num_cat = Categories.objects.count()
        num_rec = Recipes.objects.count()

        self.assertEqual(1,num_cat)
        self.assertEqual(1,num_rec)

