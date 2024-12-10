from enum import Enum  # Import Enum to create enumerators
import unittest  # Import the unittest module for testing

# defines enumerators for drink sizes.
class Size(Enum):
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"
    MEGA = "mega"

# defines enumerators for drink bases.
class Base(Enum):
    WATER = "water"
    SPRITE = "sprite"
    POKEACOLA = "pokecola"
    MR_SALT = "Mr. Salt"
    HILL_FOG = "hill fog"
    LEAF_WINE = "leaf wine"

# define enumerators for drink flavors.
class Flavor(Enum):
    LEMON = "lemon"
    CHERRY = "cherry"
    STRAWBERRY = "strawberry"
    MINT = "mint"
    BLUEBERRY = "blueberry"
    LIME = "lime"

class Drink:
    """Represents a drink with a base, size, and flavors."""
    
    # list of valid bases and flavors for the drinks.
    _valid_bases = {base for base in Base}  
    _valid_flavors = {flavor for flavor in Flavor}
    _size_costs = {
        Size.SMALL: 1.50,
        Size.MEDIUM: 1.75,
        Size.LARGE: 2.05,
        Size.MEGA: 2.15
    }

    def __init__(self, base: Base, size: Size):
        """Initializes a drink with a base and size, and an empty set of flavors."""
        self._base = base  # sets a base for the drink.
        self._size = size  # sets a size for the drink.
        self._flavors = set()  # initializes an empty set for flavors.
        self._cost = self._size_costs[size]  # sets the initial cost based on size.

    def get_base(self):
        """returns the base of the drink."""
        return self._base

    def get_flavors(self):
        """returns a list of flavors added to the drink."""
        return list(self._flavors)

    def get_num_flavors(self):
        """returns the number of different flavors added to the drink."""
        return len(self._flavors)

    def get_total(self):
        """returns the total cost of the drink."""
        return self._cost

    def add_flavor(self, flavor: Flavor):
        """adds a flavor to the drink if it's valid and not already added."""
        if flavor in self._valid_flavors:  # checks if the flavor is valid.
            if flavor not in self._flavors:  # checks if the flavor is already added.
                self._cost += 0.15  # increases the cost for each new flavor.
            self._flavors.add(flavor)  # adds the flavor to the set
        else:
            raise ValueError(f"Pick a proper flavor from {self._valid_flavors}.")

    def set_flavors(self, flavors):
        """sets multiple flavors at once, ensuring they are valid."""
        for flavor in flavors:  # iterates through the provided flavors.
            if flavor not in self._valid_flavors:  
                raise ValueError(f"Pick a proper flavor from {self._valid_flavors}.")
        self._flavors = set(flavors)  # updates the flavors set with the new valid flavors.

class Food:
    #defines food.
    _food_price = {
        "hotdog": 2.30,
        "corndog": 2.00,
        "ice_cream": 3.00,
        "onion_rings": 1.75,
        "french_fries": 1.50,
        "tater_tots": 1.70,
        "nacho_chips": 1.90
    }
    
    #defines toppings.
    _topping_price = {
        "cheery": 0.00,
        "whipped_cream": 0.00,
        "caramel_sauce:": 0.50,
        "chocolate_sauce": 0.50,
        "nacho_cheese": 0.30,
        "chili": 0.60,
        "bacon_bits": 0.30,
        "ketchup": 0.00,
        "mustard": 0.00
    }
    
    def __init__(self, food_type):
       if food_type.lower() not in self._food_price:
           raise ValueError(f"Invalid food type.")
       self._type = food_type.lower
       self._toppings = set()
       self._base_price = self._food_price[self._type]
    
    #Accessor for the base price
    def get_base_price(self):
        return self._base_price
    
    #Accessor for food type.
    def get_type(self):
        return self._type
    
    #adds toppings.
    def add_topping(self, topping):
        if topping.lower() not in self._topping_price:
            raise ValueError(f"Invalid topping")
        self._toppings.add(topping.lower())
    
    #counts the number of toppings.   
    def get_num_toppings(self):
        return list(self._toppings)
    
    def get_total_price(self):
        toppings_cost = sum(self._topping_price[topping] for topping in self._toppings)
        return self._base_price + toppings_cost
    
    
class Order:
    """represents an order containing multiple drinks."""
    
    _tax_rate = 0.0725 

    def __init__(self):
        """initializes an empty order with no drinks."""
        self._items = [] 

    def get_items(self):
        """returns the list of drinks in the order."""
        return self._items

    def get_total(self):
        """returns the total cost of all drinks in the order."""
        return sum(drink.get_total() for drink in self._items)  #calculates the total cost of all drinks.

    def get_num_items(self):
        """returns the number of drinks in the order."""
        return len(self._items)  # counts of items in the order.

    def get_tax(self):
        """calculates the tax based on the total cost of the order."""
        return self.get_total() * self._tax_rate  # calculates tax based on total.

    def get_receipt(self):
        """generates a receipt for the order."""
        receipt_data = {
            "number_drinks": self.get_num_items(),
            "drinks": [],  # a list to hold the drink details.
            "subtotal": self.get_total(),  # total cost before tax.
            "tax": self.get_tax(),  # tax amount.
            "grand_total": self.get_total() + self.get_tax()  # total cost including taxes.
        }

        for drink in self._items:  # loops through each drink in the order.
            drink_data = {
                "base": drink.get_base().value, 
                "size": drink._size.value, 
                "flavors": [flavor.value for flavor in drink.get_flavors()],  # list of flavors.
                "total_cost": drink.get_total() 
            }
            receipt_data["drinks"].append(drink_data)  # adds the drink details to the receipt.
        return receipt_data

    def add_item(self, item):
        """adds a drink to the order."""
        if isinstance(item, (Drink, Food)):  # checks if the item is a Drink instance.
            self._items.append(item)  # adds the drink to the order.
        else:
            raise ValueError("You can only add drinks or food to this order.")

    def remove_item(self, index):  # removes a drink from the order by its index.
        """removes a drink from the order by its index."""
        if 0 <= index < len(self._items):  # checks if the index is valid.
            self._items.pop(index)  # removes the drink at the specified index.
        else:
            raise IndexError("Invalid index, cannot remove item.")  # raises an error if index is invalid.

# Unit tests for the Drink and Order classes
class TestDrinkOrder(unittest.TestCase):
    """Test cases for the Drink and Order classes."""

    def test_drink_creation(self):
        """Test creating a drink with valid base and size."""
        drink = Drink(Base.WATER, Size.SMALL)  # creates a drink.
        self.assertEqual(drink.get_base(), Base.WATER)  # checks if the base is correct.
        self.assertEqual(drink.get_total(), 1.50)  # checks if the initial cost is correct.

    def test_add_flavor(self):
        """Test adding a flavor to a drink."""
        drink = Drink(Base.WATER, Size.SMALL)  # creates a drink.
        drink.add_flavor(Flavor.LEMON)  # adds a flavor.
        self.assertIn(Flavor.LEMON, drink.get_flavors())  # checks if the flavor was added.

    def test_food_creation(self):
        """Test creating a food item with a valid type."""
        food = Food("hotdog")  # Create a food item
        self.assertEqual(food.get_type(), "hotdog")  # Check if the type is correct
        self.assertEqual(food.get_base_price(), 2.30)  # Check if the base price is correct

    def test_invalid_food_creation(self):
        """Test creating a food item with an invalid type."""
        with self.assertRaises(ValueError):
            Food("invalid_food")  # Should raise a ValueError

    def test_add_topping(self):
        """Test adding a valid topping to the food item."""
        food = Food("hotdog")  # Create a food item
        food.add_topping("cherry")  # Add a topping
        self.assertEqual(food.get_num_toppings(), 1)  # Check if the number of toppings is correct

    def test_total_price_with_toppings(self):
        """Test calculating the total price of the food item including toppings."""
        food = Food("french_fries")  # Create a food item
        food.add_topping("bacon_bits")  # Add a topping
        food.add_topping("chili")  # Add another topping
        self.assertEqual(food.get_total_price(), 2.30 + 0.30 + 0.60)  # Check total price

    def test_total_price_no_toppings(self):
        """Test total price of food item with no toppings."""
        food = Food("corndog")  # Create a food item


if __name__ == '__main__':
   unittest.main()        
        
        
        
        
    
        
    
    
    
    
    