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
    recipe = graphene.Field(RecipeType, id=graphene.ID())
    recipes = graphene.List(RecipeType, )

    ingredient = graphene.Field(IngredientType, id=graphene.ID())
    ingredients = graphene.List(IngredientType, ingredients_in=graphene.List(of_type=graphene.ID))
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
        ingredients_in = kwargs.get('ingredients')
        if ingredients_in is not None:
            return Recipe.objects.filter(ingredients__in=ingredients_in)

        return Recipe.objects.all()

    def resolve_ingredients(self, info, **kwargs):
        return Ingredient.objects.all()
