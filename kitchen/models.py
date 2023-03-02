from django.db import models


class DishType(models.Model):
    name = models.CharField(max_length=255)


class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField()
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE)
