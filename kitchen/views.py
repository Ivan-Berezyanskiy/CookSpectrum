from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Cook, DishType, Dish
from django.views import generic


@login_required
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


class CookListView(generic.ListView, LoginRequiredMixin):
    model = Cook
    

class CookDetailView(generic.DetailView, LoginRequiredMixin):
    model = Cook

    def get_context_data(self, *args, **kwargs):
        context = super(CookDetailView, self).get_context_data()
        context["user.id"] = self.request.user.id
        return context


class CookUpdateView(generic.UpdateView, LoginRequiredMixin):
    model = Cook
    fields = "__all__"

    def get_success_url(self):
        return reverse_lazy("kitchen:cook-detail", kwargs={"pk": self.kwargs["pk"]})


class CookDeleteView(generic.DeleteView, LoginRequiredMixin):
    model = Cook
    success_url = reverse_lazy("kitchen:cook-list")


class DishTypeListView(generic.ListView, LoginRequiredMixin):
    model = DishType
    context_object_name = "dish_type_list"
    template_name = "kitchen/dish_type_list.html"


class DishTypeDetailView(generic.DetailView, LoginRequiredMixin):
    model = DishType
    context_object_name = "dish_type_detail"
    template_name = "kitchen/dish_type_detail.html"


class DishTypeCreateView(generic.CreateView, LoginRequiredMixin):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish-type-list")
    template_name = "kitchen/dish_type_form.html"


class DishTypeUpdateView(generic.UpdateView, LoginRequiredMixin):
    model = DishType
    fields = "__all__"
    template_name = "kitchen/dish_type_form.html"

    def get_success_url(self):
        return reverse_lazy("kitchen:dish-type-detail", kwargs={"pk": self.kwargs["pk"]})


class DishTypeDeleteView(generic.DeleteView, LoginRequiredMixin):
    model = DishType
    success_url = reverse_lazy("kitchen:dish-type-list")
    template_name = "kitchen/dish_type_confirm_delete.html"


class DishListView(generic.ListView, LoginRequiredMixin):
    model = Dish
    queryset = Dish.objects.prefetch_related("dish_type")


class DishDetailView(generic.DetailView, LoginRequiredMixin):
    model = Dish


class DishCreateView(generic.CreateView, LoginRequiredMixin):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish-list")


class DishUpdateView(generic.UpdateView, LoginRequiredMixin):
    model = Dish
    fields = "__all__"

    def get_success_url(self):
        return reverse_lazy("kitchen:dish-detail", kwargs={"pk": self.kwargs["pk"]})


class DishDeleteView(generic.DeleteView, LoginRequiredMixin):
    model = Dish
    success_url = reverse_lazy("kitchen:dish-list")
