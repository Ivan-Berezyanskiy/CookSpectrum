from django.shortcuts import render
from django.urls import reverse_lazy

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


class DishTypeListView(generic.ListView):
    model = DishType
    context_object_name = "dish_type_list"
    template_name = "kitchen/dish_type_list.html"


class DishTypeDetailView(generic.DetailView):
    model = DishType
    context_object_name = "dish_type_detail"
    template_name = "kitchen/dish_type_detail.html"


class DishTypeCreateView(generic.CreateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish-types-list")
    template_name = "kitchen/dish_type_form.html"


class DishTypeUpdateView(generic.UpdateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish-types-list")
    template_name = "kitchen/dish_type_form.html"


class DishTypeDeleteView(generic.DeleteView):
    model = DishType
    success_url = reverse_lazy("kitchen:dish-types-list")
    template_name = "kitchen/dish_type_delete.html"


class DishListView(generic.ListView):
    model = Dish
