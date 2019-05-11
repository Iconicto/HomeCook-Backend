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


class Query(graphene.ObjectType):
    recipes = graphene.List(RecipeType)
    ingredients = graphene.List(IngredientType)
    steps = graphene.List(StepType)

    def resolve_recipes(self, info, **kwargs):
        return Recipe.objects.all()

    def resolve_ingredients(self, info, **kwargs):
        return Ingredient.objects.all()

    def resolve_steps(self, info, **kwargs):
        return Step.objects.all()
