from django.shortcuts import render
from .models import Cook, DishType, Dish
from django.views import generic


def index(request):
    """View function for home page of site."""
    num_dishes = Dish.objects.count()
    num_dishtypes = DishType.objects.count()
    num_cooks = Cook.objects.count()

    context = {
        "num_dishes": num_dishes,
        "num_dishtypes": num_dishtypes,
        "num_cooks": num_cooks,
    }

    return render(request, "kitchen/index.html", context=context)


class CookListView(generic.ListView):
    model = Cook
