from django.contrib.auth import get_user_model
from django.test import TestCase
from django.test import RequestFactory
from django.urls import reverse

from kitchen.models import DishType, Cook, Dish
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
    def setUp(self) -> None:
        self.dishtype = DishType.objects.create(
            name="test_name",
        )
        self.dish = Dish.objects.create(
            price=12.05,
            name="test_dish",
            dish_type=self.dishtype
        )

    def test_dish_list_login_required(self):
        res = self.client.get(reverse("kitchen:dish-list"))
        self.assertNotEqual(res.status_code, 200)

    def test_dish_detail_login_required(self):
        res = self.client.get(reverse(
            "kitchen:dish-detail",
            kwargs={"pk": self.dish.id}
        ))
        self.assertNotEqual(res.status_code, 200)

    def test_dish_create_login_required(self):
        res = self.client.get(reverse("kitchen:dish-create"))
        self.assertNotEqual(res.status_code, 200)

    def test_dish_update_login_required(self):
        res = self.client.get(reverse(
            "kitchen:dish-update", kwargs={"pk": self.dish.id}
        ))
        self.assertNotEqual(res.status_code, 200)

    def test_dish_delete_login_required(self):
        res = self.client.get(reverse(
            "kitchen:dish-delete", kwargs={"pk": self.dish.id}
        ))
        self.assertNotEqual(res.status_code, 200)


class PrivateDishTypeTest(OnlyLoggedIn, TestCase):

    def setUp(self) -> None:
        self.dishtype = DishType.objects.create(
            name="test_name",
        )

    def test_dishtype_list_login_required(self):
        res = self.client.get(reverse("kitchen:dish-type-list"))
        self.assertNotEqual(res.status_code, 200)

    def test_dishtype_create_login_required(self):
        res = self.client.get(reverse("kitchen:dish-type-create"))
        self.assertNotEqual(res.status_code, 200)

    def test_dishtype_update_login_required(self):
        res = self.client.get(reverse(
            "kitchen:dish-type-update",
            kwargs={"pk": self.dishtype.id}
        ))
        self.assertNotEqual(res.status_code, 200)

    def test_dishtype_delete_login_required(self):
        res = self.client.get(reverse(
            "kitchen:dish-type-delete",
            kwargs={"pk": self.dishtype.id}
        ))
        self.assertNotEqual(res.status_code, 200)


class PublicCookTest(OnlyLoggedIn, TestCase):

    def setUp(self) -> None:
        self.cook = get_user_model().objects.create_user(
            username="test_username",
            password="1234qwer"
        )

    def test_cook_list_login_required(self):
        res = self.client.get(reverse("kitchen:cook-list"))
        self.assertNotEqual(res.status_code, 200)

    def test_cook_detail_login_required(self):
        res = self.client.get(reverse(
            "kitchen:cook-detail",
            kwargs={"pk": self.cook.id}
        ))
        self.assertNotEqual(res.status_code, 200)

    def test_cook_create_login_required(self):
        res = self.client.get(reverse("kitchen:registration"))
        self.assertNotEqual(res.status_code, 200)

    def test_cook_delete_login_required(self):
        res = self.client.get(reverse(
            "kitchen:cook-delete",
            kwargs={"pk": self.cook.id}
        ))
        self.assertNotEqual(res.status_code, 200)
