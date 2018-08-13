import graphene
from graphql import GraphQLError

from graphene_django.types import DjangoObjectType


from api.models import Categories
from api.utilities.utility import (
    validate_empty_strings,
    update_entity_fields
)

class CategoriesType(DjangoObjectType):
    class Meta:
        model = Categories


class Query(graphene.AbstractType):
        all_categories = graphene.List(CategoriesType)
        get_category = graphene.Field(
            CategoriesType,
            id = graphene.Int()
        )

        def resolve_all_categories(self,info,*kwargs):
            return Categories.objects.all()

        def resolve_get_category(self,info,id):
            try:
                exact_category = Categories.objects.get(pk=id)
            except:
                raise GraphQLError("category does not exist")
            return exact_category


class CreateCategory(graphene.Mutation):
    class Arguments:
        category_title = graphene.String()
        category_description = graphene.String()

    category = graphene.Field(CategoriesType)
    def mutate(self,info,**kwargs):
        validate_empty_strings(**kwargs)
        cat = Categories(**kwargs)
        cat.save()

        return CreateCategory(category=cat)

class UpdateCategory(graphene.Mutation):
    class Arguments:
        id = graphene.Int()
        category_title = graphene.String()
        category_description = graphene.String()

    category = graphene.Field(CategoriesType)
    def mutate(self,info,id,**kwargs):
        validate_empty_strings(**kwargs)
        try:
            exact_category = Categories.objects.get(pk=id)
            update_entity_fields(exact_category, **kwargs)
            exact_category.save()
            return UpdateCategory(category=exact_category)
        except:
            raise GraphQLError("Category not found")

class DeleteCategory(graphene.Mutation):
    message = graphene.String()
    class Arguments:
        id = graphene.Int()
    def mutate(self,info,id):
        try:
            exact_category = Categories.objects.get(pk=id)
            exact_category.delete()            
            event = "Category with id {} has been deleted".format(id)
            return DeleteCategory(message=event)
        except:
            raise GraphQLError("Category not found")


class Mutation(graphene.ObjectType):
    create_category = CreateCategory.Field()
    update_category = UpdateCategory.Field()
    delete_category = DeleteCategory.Field()