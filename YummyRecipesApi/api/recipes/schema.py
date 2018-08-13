import graphene

from graphene_django.types import DjangoObjectType

from api.models import Recipes


class RecipesType(DjangoObjectType):
    class Meta:
        model = Recipes

class Query(graphene.AbstractType):
        all_recipes = graphene.List(RecipesType)

        def resolve_all_recipes(self,info,*kwargs):
            return Recipes.objects.all()
