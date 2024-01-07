"""graphql_tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView #View for the user interface
from graphql_tutorial.schema import schema #Schema we want to query

urlpatterns = [
    path('admin/', admin.site.urls),
    # This URL will provide a user interface that is used to query the database
    # and interact with the GraphQL API.
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
]