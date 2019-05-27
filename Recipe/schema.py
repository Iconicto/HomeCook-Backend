import graphene
from graphene_django.types import DjangoObjectType

from .models import *


class RecipeType(DjangoObjectType):
    class Meta:
        model = Recipe


class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient


class StepType(DjangoObjectType):
    class Meta:
        model = Step


class RecipeIngredientType(DjangoObjectType):
    class Meta:
        model = RecipeIngredient


class Query(graphene.ObjectType):
    #
    recipe = graphene.Field(RecipeType, id=graphene.ID())
    ingredient = graphene.Field(IngredientType, id=graphene.ID())

    recipes = graphene.List(RecipeType, ingredients_in=graphene.List(of_type=graphene.ID))
    ingredients = graphene.List(IngredientType)

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
