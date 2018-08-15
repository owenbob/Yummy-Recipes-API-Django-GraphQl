import graphene
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
        ):
        pass


schema = graphene.Schema(query=Query, mutation=Mutation)
