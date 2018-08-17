import graphene
import graphql_jwt


import api.categories.schema
import api.recipes.schema
import api.users.schema

class Query(
        api.categories.schema.Query,
        api.recipes.schema.Query,
        api.users.schema.Query,
        graphene.ObjectType
        
        ):
        pass


class Mutation(
        api.categories.schema.Mutation,
        api.recipes.schema.Mutation,
        api.users.schema.Mutation,
        graphene.ObjectType
        ):
        login_user = graphql_jwt.ObtainJSONWebToken.Field()
        verify_token = graphql_jwt.Verify.Field()
        refresh_token = graphql_jwt.Refresh.Field()
        


schema = graphene.Schema(query=Query, mutation=Mutation)
