import unittest
from Drink_Project import Drink, Food, IceStorm, IceStormFlavor, Base, Size, Flavor

# Unit tests for the Drink and Order classes
class TestDrinkOrder(unittest.TestCase):
    """Test cases for the Drink and Order classes."""

    def test_drink_creation(self):
        drink = Drink(Base.WATER, Size.SMALL)
        self.assertEqual(drink.get_base(), Base.WATER)
        self.assertEqual(drink.get_total(), 1.50)

    def test_add_flavor(self):
        drink = Drink(Base.WATER, Size.SMALL)
        drink.add_flavor(Flavor.LEMON)
        self.assertIn(Flavor.LEMON, drink.get_flavors())
    
    def test_food_creation(self):
        food = Food("hotdog")
        self.assertEqual(food.get_type(), "hotdog")
        self.assertEqual(food.get_base_price(), 2.30)

    def test_invalid_food_creation(self):
        with self.assertRaises(ValueError):
            Food("invalid_food")

    def test_add_topping(self):
        food = Food("hotdog")
        food.add_topping("cherry")
        self.assertEqual(food.get_num_toppings(), 1)
    
    def test_total_price_no_toppings(self):
        food = Food("corndog")

    def test_ice_storm_creation(self):
        ice_storm = IceStorm(IceStormFlavor.MINT_CHOCOLATE_CHIP)
        self.assertEqual(ice_storm.get_total(), 4.00)

    def test_add_topping(self):
        ice_storm = IceStorm(IceStormFlavor.CHOCOLATE)
        ice_storm.add_topping("cherry")
        self.assertEqual(ice_storm.get_num_flavors(), 1)

    def test_total_price_with_toppings(self):
        ice_storm = IceStorm(IceStormFlavor.VANILLA_BEAN)
        ice_storm.add_topping("caramel_sauce")
        ice_storm.add_topping("cookie_dough")
        self.assertEqual(ice_storm.get_total(), 3.00 + 0.50 + 1.00)

if __name__ == '__main__':
    unittest.main()