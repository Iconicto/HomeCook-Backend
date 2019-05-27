import graphene
from graphene import Node
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType

from .models import *


class RecipeType(DjangoObjectType):
    class Meta:
        model = Recipe
        interfaces = (Node,)
        filter_fields = {
            'id': ['exact'],
            'name': ['exact', 'icontains', 'istartswith', 'iendswith'],
            'description': ['exact', 'icontains', 'istartswith', 'iendswith'],
            'rating': ['exact', 'gte', 'lte', 'gt', 'lt', 'range'],
            'prepTime': ['exact', 'gte', 'lte', 'gt', 'lt', 'range'],
            'calories': ['exact', 'gte', 'lte', 'gt', 'lt', 'range'],
            'isPopular': ['exact'],
            'ingredients': ['in'],
        }
        # filter_fields = [
        #     'name',
        #     'description',
        #     'rating',
        #     'prepTime',
        #     'calories',
        #     'isPopular',
        # ]


class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient
        # interfaces = (Node,)
        # filter_fields = {
        #     'name': ['exact', 'icontains', 'istartswith', 'iendswith'],
        #     'description': ['exact', 'icontains', 'istartswith', 'iendswith'],
        # }
        # filter_fields = ['name', 'description']


class StepType(DjangoObjectType):
    class Meta:
        model = Step
        # interfaces = (Node,)
        # filter_fields = {
        #     'stepNumber': ['exact', 'gte', 'lte', 'gt', 'lt', 'range'],
        #     'instruction': ['exact', 'icontains', 'istartswith', 'iendswith'],
        #     'description': ['exact', 'icontains', 'istartswith', 'iendswith', 'isnull'],
        # }


class RecipeIngredientType(DjangoObjectType):
    class Meta:
        model = RecipeIngredient
        # interfaces = (Node,)
        # filter_fields = {
        #     'quantity': ['exact', 'gte', 'lte', 'gt', 'lt', 'range'],
        #     'unit': ['exact', 'icontains', 'istartswith', 'iendswith', 'isnull'],
        # }


class Query(graphene.ObjectType):
    # recipes = graphene.List(RecipeType)
    #
    recipe = Node.Field(RecipeType)
    recipes = DjangoFilterConnectionField(RecipeType)

    ingredient = Node.Field(IngredientType)
    ingredients = graphene.List(IngredientType)
    # ingredients = DjangoFilterConnectionField(IngredientType)

    def resolve_recipe(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Recipe.objects.get(pk=id)

        return None

    def resolve_ingredient(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Ingredient.objects.get(pk=id)

        return None

    def resolve_recipes(self, info, **kwargs):
        return Recipe.objects.all()

    def resolve_ingredients(self, info, **kwargs):
        return Ingredient.objects.all()
