from django.db import models
from recipe.models import Ingredient

# Create your models here.

class IngredientSwap(models.Model):
    original_ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='original_ingredient')
    substitute_ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='substitute_ingredient')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.original_ingredient.name} -> {self.substitute_ingredient.name}" 
