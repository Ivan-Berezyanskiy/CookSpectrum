from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class CookAdminTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_ = get_user_model().objects.create_superuser(
            username="admin123",
            password="admintestpass"
        )
        self.client.force_login(self.admin_)
        self.cook = get_user_model().objects.create_user(
            username="admin1223",
            password="admintestspass",
            first_name="Volkswagen",
            last_name="Germany",
            years_of_experience=5
        )

    def test_cook_years_of_experience(self):
        url = reverse("admin:kitchen_cook_changelist")
        res = self.client.get(url)

        self.assertContains(res, self.cook.years_of_experience)

    def test_cook_detailed_years_of_experience(self):
        url = reverse("admin:kitchen_cook_change", args=[self.cook.id])
        response = self.client.get(url)

        self.assertContains(response, self.cook.years_of_experience)
