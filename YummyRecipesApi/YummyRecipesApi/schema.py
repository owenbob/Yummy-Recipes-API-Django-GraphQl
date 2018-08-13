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
<<<<<<< HEAD
        api.categories.schema.Mutation,
        api.recipes.schema.Mutation
=======
        api.categories.schema.Mutation
>>>>>>>  #159546225  CRUD for categories (#7)

        ):
        pass

<<<<<<< HEAD
schema = graphene.Schema(query=Query, mutation=Mutation)
=======
schema = graphene.Schema(query=Query, mutation=Mutation)
>>>>>>>  #159546225  CRUD for categories (#7)
