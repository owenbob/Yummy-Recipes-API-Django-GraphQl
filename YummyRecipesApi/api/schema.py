# import graphene

# from graphene_django.types import DjangoObjectType

# from .models import (
#     Categories,
#     Recipes
# )


# class CategoriesType(DjangoObjectType):
#     class Meta:
#         model = Categories


# class RecipesType(DjangoObjectType):
#     class Meta:
#         model = Recipes

# class Query(graphene.AbstractType):
#         all_categories= graphene.List(CategoriesType)
#         all_recipes = graphene.List(RecipesType)


#         def resolve_all_categories(self,info,*kwargs):
#             return Categories.objects.all()

#         def resolve_all_recipes(self,info,*kwargs):
#             return Recipes.objects.all()
