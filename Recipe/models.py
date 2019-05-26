from django.db import models


# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    # steps
    # ingredients
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    prepTime = models.DecimalField(max_digits=5, decimal_places=2)
    calories = models.IntegerField()
    dishImage = models.ImageField(upload_to='Recipe/DishImages/')
    bannerImage = models.ImageField(upload_to='Recipe/Banners/')

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='Ingredients/')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Step(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='steps', on_delete=models.CASCADE)
    stepNumber = models.IntegerField()
    instruction = models.TextField()
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='StepInstructions/', blank=True)

    def __str__(self):
        return "{} - Step #{}".format(self.recipe.name, self.stepNumber)


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='ingredients', on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, related_name='ingredients', on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=15, default='',
                            choices=(
                                ('ml', 'milliliters'),
                                ('cups', 'cups'),
                                ('liter', 'liters'),
                                ('teaspoon', 'teaspoon'),
                                ('tablespoon', 'tablespoon'),
                                ('liter', 'liters'),
                                ('oz', 'ounce'),
                                ('gram', 'grams'),
                                ('', ''),
                            ))

    def __str__(self):
        return "{} - {}".format(self.recipe.name, self.ingredient)
