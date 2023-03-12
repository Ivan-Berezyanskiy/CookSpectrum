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

    def test_cook_creation_form_with_years_of_experience_is_valid(self):
        self.assertTrue(self.cook.is_valid())
        self.assertEqual(self.cook.cleaned_data, self.form_data)

    def test_years_of_experience_negative_number(self):
        self.form_data["years_of_experience"] = -1
        form = CookCreationForm(data=self.form_data)
        self.assertFalse(form.is_valid())

    def test_years_of_experience_more_than_correct(self):
        self.form_data["years_of_experience"] = 100
        form = CookCreationForm(data=self.form_data)
        self.assertFalse(form.is_valid())

    def test_years_of_experience_correct_data(self):
        self.form_data["years_of_experience"] = 20
        form = CookCreationForm(data=self.form_data)
        self.assertTrue(form.is_valid())
