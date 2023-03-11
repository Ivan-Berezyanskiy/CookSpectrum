from django.test import TestCase

from kitchen.forms import CookCreationForm


class FormsTests(TestCase):
    def setUp(self):
        self.form_data = {
            "username": "admin1223",
            "password1": "admintestspass",
            "password2": "admintestspass",
            "first_name": "Volkswagen",
            "last_name": "Germany",
            "years_of_experience": 22
        }
        self.cook = CookCreationForm(data=self.form_data)

    def test_cook_creation_form_with_years_of_experience_name_is_valid(self):
        self.assertTrue(self.cook.is_valid())
        self.assertEqual(self.cook.cleaned_data, self.form_data)
