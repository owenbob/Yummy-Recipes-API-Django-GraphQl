import graphene
import api.categories.schema
import api.recipes.schema

class Query(
        api.categories.schema.Query,
        api.recipes.schema.Query,
        graphene.ObjectType
        
        ):
        pass


class Mutation(
        api.categories.schema.Mutation

        ):
        pass

schema = graphene.Schema(query=Query, mutation=Mutation)