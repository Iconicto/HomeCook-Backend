import graphene
from graphene_django import DjangoObjectType

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
    recipes = graphene.List(RecipeType)
    ingredients = graphene.List(IngredientType)
    steps = graphene.List(StepType)
    recipe_ingredients = graphene.List(RecipeIngredient)

    def resolve_recipes(self, info, **kwargs):
        return Recipe.objects.all()

    def resolve_ingredients(self, info, **kwargs):
        return Ingredient.objects.all()

    def resolve_steps(self, info, **kwargs):
        return Step.objects.all()

    def resolve_recipe_ingredients(self, info, **kwargs):
        return RecipeIngredient.objects.all()
