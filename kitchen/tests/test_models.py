from django.test import TestCase

from kitchen.models import Dish, DishType, Cook


class ModelDishTypeTests(TestCase):
    def test_str(self):
        dishtype = DishType.objects.create(
            name="Antarctica"
        )
        self.assertEqual(
            dishtype.__str__(),
            dishtype.name
        )


class ModelCookTests(TestCase):
    def setUp(self):
        self.years_of_experience_ = 3
        self.cook_ = Cook.objects.create_user(
            years_of_experience=self.years_of_experience_,
            username="TestCook",
            password="qwerty123Cook",
            last_name="Testa",
            first_name="Testov"
        )

    def test_years_of_experience(self):
        self.assertEqual(
            self.cook_.years_of_experience,
            self.years_of_experience_
        )

    def test_str(self):
        self.assertEqual(
            self.cook_.__str__(),
            f"{self.cook_.username} "
            f"({self.cook_.first_name} {self.cook_.last_name})")


class ModelDishTests(TestCase):
    def test_str(self):
        dishtype_ = DishType.objects.create(
            name="Test",
        )

        dish = Dish.objects.create(
            price=40,
            name="TestModel",
            dish_type=dishtype_
        )
        self.assertEqual(dish.__str__(), dish.name)
