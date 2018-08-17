import graphene
from graphql import GraphQLError
from graphql_jwt.decorators import login_required

from graphene_django import DjangoObjectType
from django.contrib.auth import get_user_model


User = get_user_model()


class UserType(DjangoObjectType):
    class Meta:
        model = User
class Query(graphene.ObjectType):
    users = graphene.List(UserType)

    @login_required
    def resolve_users(self, info):
        all_users = User.objects.all()
        return all_users

class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    def mutate(self, info, username, password, email):
        user = User(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()

        return CreateUser(user=user)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()