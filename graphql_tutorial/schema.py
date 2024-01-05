import graphene
from graphene_django import DjangoObjectType #used to change Django object into a format that is readable by GraphQL
from app.models import Blog

class BlogType(DjangoObjectType):
    # Describe the data that is to be formatted into GraphQL fields
    class Meta:
        model= Blog
        field= ["title", "created", "body"]

class Query(graphene.ObjectType):
    #query BlogType to get list of blogs
    blog_list=graphene.List(BlogType)
    blog_data = graphene.Field(BlogType, id=graphene.Int()) # id=graphene.Int() gives id an integer datatype

    def resolve_blog_list(root, info):
        # We can easily optimize query count in the resolve method
        return Blog.objects.all()
    def resolve_blog_data(root, info, id):
        # get data where id in the database = id queried from the frontend
        return Blog.objects.get(id=id)

class BlogMutation(graphene.Mutation):
    class Arguments:
        # Add fields you would like to create. This will corelate with the BlogType fields above.
        title=graphene.String()
        body=graphene.String()
        created=graphene.DateTime()

    blog = graphene.Field(BlogType) # define the class we are getting the fields from
    @classmethod
    def mutate(cls, root, info, title, body, created):
        # function that will save the data
        blog = Blog(title=title, body=body, created=created) #accepts all fields
        blog.save() #d=save the blog

class Mutation(graphene.ObjectType):
    # keywords that will be used to do the mutation in the frontend
    create_blog= BlogMutation.Field()     

schema = graphene.Schema(query=Query, mutation=Mutation)