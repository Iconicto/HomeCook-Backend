import graphene
import Recipe.schema


class Query(Recipe.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
