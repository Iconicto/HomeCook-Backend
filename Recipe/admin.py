from django.contrib import admin
from .models import *


# Register your models here.

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'rating', 'prepTime', 'calories', 'dishImage', 'bannerImage')
    list_display_links = list_display


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image')
    list_display_links = list_display


class StepAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'stepNumber', 'instruction', 'description', 'image')
    list_display_links = list_display


class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'ingredient', 'quantity', 'unit')
    list_display_links = list_display


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Step, StepAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
