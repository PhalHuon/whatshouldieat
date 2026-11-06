from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)

class Recipe(models.Model):
    recipe_id = models.CharField(max_length=50, primary_key=True)
    title = models.CharField(max_length=250)
    instructions = models.TextField()

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)  # If parent deleted, all child deleted too
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)  # blocks any delete
    quantity = models.FloatField(blank=True, null=True)  # null = database level, blank = form level
    unit = models.CharField(max_length=50, blank=True)
    original_text = models.TextField()