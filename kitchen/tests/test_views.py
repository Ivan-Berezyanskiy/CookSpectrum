from django.contrib.auth import get_user_model
from django.test import TestCase
from django.test import RequestFactory
from django.urls import reverse

from kitchen.models import DishType
from kitchen.views import DishTypeListView

DISHTYPE_URL = reverse("kitchen:dish-type-list")


class OnlyLoggedIn(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="admin",
            password="admin123"
        )

        self.client.force_login(self.user)


class PublicDishTypeTest(TestCase):
    def test_login_required(self) -> None:
        response = self.client.get(DISHTYPE_URL)

        self.assertNotEqual(response.status_code, 200)


class PrivateDishTypeTest(OnlyLoggedIn, TestCase):
    def setUp(self) -> None:
        DishType.objects.create(
            name="Tesew",
        )
        DishType.objects.create(
            name="Apple",
        )

    def test_retrieve_dishtypes(self) -> None:
        response = self.client.get(DISHTYPE_URL)
        dishtypes = DishType.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["dishtype_list"]),
            list(dishtypes)
        )
        self.assertTemplateUsed(response, "kitchen/dish-type-list.html")

    def test_get_queryset(self):
        name = "Apple"
        request = RequestFactory().get("kitchen:dish-type-list")
        request.GET = {"name": name}
        view = DishTypeListView()
        view.request = request
        dishtypes = DishType.objects.all()

        queryset = view.get_queryset()

        self.assertQuerysetEqual(queryset, (dishtypes.filter(
            name__icontains=name
        )))


class PrivateCookTest(OnlyLoggedIn, TestCase):

    def test_create_cook(self):
        form_data = {
            "username": "test",
            "password1": "test12345",
            "password2": "test12345",
            "first_name": "Volkswagen",
            "last_name": "Germany",
            "years_of_experience": "4"
        }
        self.client.post(reverse("kitchen:cook-create"), data=form_data)
        new_user = get_user_model().objects.get(username=form_data["username"])

        self.assertEqual(new_user.first_name, form_data["first_name"])
        self.assertEqual(new_user.last_name, form_data["last_name"])
        self.assertEqual(new_user.years_of_experience, form_data["years_of_experience"])

    def test_delete_cook(self):
        cook = get_user_model().objects.create(
            username="not_admin.user",
            years_of_experience="12",
            first_name="Not Admin",
            last_name="User",
            password="1qazcde3",
        )
        response = self.client.post(
            reverse("kitchen:cook-delete", kwargs={"pk": cook.id})
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(
            get_user_model().objects.filter(id=cook.id).exists()
        )
