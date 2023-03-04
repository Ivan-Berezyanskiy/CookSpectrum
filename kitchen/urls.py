from django.urls import path

from kitchen.views import (
    index,
    CookListView,
    DishTypeListView,
    DishListView,
    DishTypeDetailView,
    DishTypeCreateView,
    DishTypeUpdateView,
    DishTypeDeleteView,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "cooks/",
        CookListView.as_view(),
        name="cooks-list",
    ),
    path(
        "dish-types/",
        DishTypeListView.as_view(),
        name="dish-types-list",
    ),
    path(
        "dish-types/<int:pk>/",
        DishTypeDetailView.as_view(),
        name="dish-types-detail",
    ),
    path(
        "dish-types/create",
        DishTypeCreateView.as_view(),
        name="dish-types-create",
    ),
    path(
        "dish-types/<int:pk>/update",
        DishTypeUpdateView.as_view(),
        name="dish-types-update",
    ),
    path(
        "dish-types/<int:pk>/delete",
        DishTypeDeleteView.as_view(),
        name="dish-types-delete",
    ),
    path(
        "dishes/",
        DishListView.as_view(),
        name="dish-list",
    ),
]

app_name = "kitchen"
