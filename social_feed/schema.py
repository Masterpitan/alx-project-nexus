import graphene
import feed.schema

class Query(feed.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)
