import graphene
from graphql import GraphQLError
from graphql_jwt.decorators import login_required

from graphene_django.types import DjangoObjectType

from api.models import (
    Categories,
    Recipes
)
from api.utilities.utility import (
    validate_empty_strings,
    update_entity_fields
    )


class RecipesType(DjangoObjectType):
    class Meta:
        model = Recipes

class Query(graphene.AbstractType):
        all_recipes = graphene.List(RecipesType)
        get_one_recipe = graphene.Field(
                            RecipesType,
                            recipe_id = graphene.Int()
                            )

        @login_required
        def resolve_all_recipes(self,info,*kwargs):
            return Recipes.objects.all()


        @login_required
        def resolve_get_one_recipe(self,info,recipe_id):

            exact_recipe = Recipes.objects.get(id=recipe_id)
            import pdb; pdb.set_trace()
            return exact_recipe

class CreateRecipe(graphene.Mutation):
    class Arguments:
        category_id = graphene.Int()
        recipe_title = graphene.String()
        recipe_description = graphene.String()

    recipe = graphene.Field(RecipesType)

    @login_required
    def mutate(self,info,category_id,**kwargs):
        category = Categories.objects.get(id=category_id)
        if  not category:
            raise GraphQLError("Category Id provided does not match any existant Id")

        validate_empty_strings(**kwargs)
        recipe = Recipes(category_id=category_id,**kwargs)
        recipe.save()
        return CreateRecipe(recipe=recipe)

class UpdateRecipe(graphene.Mutation):
    class Arguments:
        recipe_id=graphene.Int()
        recipe_title = graphene.String()
        recipe_description = graphene.String()

    recipe = graphene.Field(RecipesType)

    @login_required
    def mutate(self,info,recipe_id,**kwargs):
        validate_empty_strings(**kwargs)
        exact_recipe = Recipes.objects.get(id=recipe_id)

        if exact_recipe:
            update_entity_fields(exact_recipe,**kwargs)
            exact_recipe.save()
            return UpdateRecipe(recipe=exact_recipe)
        else:
            raise GraphQLError("Recipe with Id {} does not exist".format(recipe_id))


class DeleteRecipe(graphene.Mutation):
    message = graphene.String()
    class Arguments:
        recipe_id = graphene.Int()

    @login_required
    def mutate(self,info,recipe_id):
        recipe = Recipes.objects.get(id=recipe_id)
        if not recipe:
            raise GraphQLError("Recipe Id does not exist" )
        recipe.delete()
        event = "Recipe with id {} has been deleted".format(recipe_id)
        return DeleteRecipe(message=event)

class Mutation(graphene.ObjectType):
    create_recipe = CreateRecipe.Field()
    update_recipe = UpdateRecipe.Field()
    delete_recipe = DeleteRecipe.Field()
