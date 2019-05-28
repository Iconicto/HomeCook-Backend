from django.db.models import Count
import graphene
from graphene_django.types import DjangoObjectType
from django.db.models import Q

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
    ingredient_name = graphene.String()
    ingredient_quantity = graphene.Float()

    class Meta:
        model = RecipeIngredient


class RecipeIngredientInputType(graphene.InputObjectType):
    id = graphene.ID(required=True)
    quantity = graphene.Float(required=True)


class Query(graphene.ObjectType):
    #
    recipe = graphene.Field(RecipeType, id=graphene.ID(required=True))
    ingredient = graphene.Field(IngredientType, id=graphene.ID(required=True))

    recipes = graphene.List(RecipeType, ingredients_in=graphene.List(of_type=graphene.ID),
                            ingredients_in_exact=graphene.List(RecipeIngredientInputType))
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
        ingredients_in = kwargs.get('ingredients_in')
        ingredients_in_exact = kwargs.get('ingredients_in_exact')
        if ingredients_in_exact is not None:
            my_filter_qs = Q()
            ingredients_ids = []
            for ingredient_in_exact in ingredients_in_exact:
                # my_filter_qs = my_filter_qs | (Q(ingredients__quantity__lte=ingredient_in_exact['quantity']
                #                                  ) | Q(ingredients__optional__exact=False))
                ingredients_ids.append(ingredient_in_exact['id'])
            print(Recipe.objects.filter(my_filter_qs).query)
            return Recipe.objects.filter(ingredients__ingredient_id__in=ingredients_ids).annotate(
                num_ingredients=Count('ingredients')).filter(num_ingredients=len(ingredients_ids))

        if ingredients_in is not None:
            return Recipe.objects.filter(ingredients__ingredient_id__in=ingredients_in).distinct()

        return Recipe.objects.all()

    def resolve_ingredients(self, info, **kwargs):
        return Ingredient.objects.all()
