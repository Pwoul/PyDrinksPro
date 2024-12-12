from enum import Enum  # Import Enum to create enumerators


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
    # defines food.
    _food_price = {
        "hotdog": 2.30,
        "corndog": 2.00,
        "ice_cream": 3.00,
        "onion_rings": 1.75,
        "french_fries": 1.50,
        "tater_tots": 1.70,
        "nacho_chips": 1.90
    }
    
    # defines toppings.
    _topping_price = {
        "cherry": 0.00,
        "whipped_cream": 0.00,
        "caramel_sauce": 0.50,
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
        self._type = food_type.lower()  # Corrected line
        self._toppings = set()
        self._base_price = self._food_price[self._type]
    
    # Accessor for the base price
    def get_base_price(self):
        return self._base_price
    
    # Accessor for food type.
    def get_type(self):
        return self._type
    
    # adds toppings.
    def add_topping(self, topping):
        if topping.lower() not in self._topping_price:
            raise ValueError(f"Invalid topping")
        self._toppings.add(topping.lower())
    
    # counts the number of toppings.   
    def get_num_toppings(self):
        return len(self._toppings)  # Return the count of toppings
    
    def get_total_price(self):
        toppings_cost = sum(self._topping_price[topping] for topping in self._toppings)
        return round(self._base_price + toppings_cost, 2)  # Round to 2 decimal places
    
class IceStormFlavor(Enum):
    MINT_CHOCOLATE_CHIP = 4.00
    CHOCOLATE = 3.00
    VANILLA_BEAN = 3.00
    BANANA = 3.50
    BUTTER_PECAN = 3.50
    SMORE = 4.00

class IceStorm:
    _topping_price = {
        "cherry": 0.00,
        "whipped_cream": 0.00,
        "caramel_sauce": 0.50,
        "chocolate_sauce": 0.50,
        "storios": 1.00,
        "dig_dogs": 1.00,
        "t_and_t": 1.00,
        "cookie_dough": 1.00,
        "pecans": 0.50
    }

    def __init__(self, flavor: IceStormFlavor):
        self._flavor = flavor
        self._toppings = set()
        self._base_price = flavor.value

    def add_flavor(self, flavor: IceStormFlavor):
        raise NotImplementedError("Ice Storms can only have one flavor.")

    def get_flavors(self):
        return list(IceStormFlavor)

    def get_base(self):
        return None

    def get_size(self):
        return None

    def get_total(self):
        toppings_cost = sum(self._topping_price[topping] for topping in self._toppings)
        return round(self._base_price + toppings_cost, 2)

    def get_num_flavors(self):
        return len(self._toppings)

    def add_topping(self, topping):
        if topping.lower() not in self._topping_price:
            raise ValueError(f"Invalid topping")
        self._toppings.add(topping.lower())

    def __str__(self):
        return f"Ice Storm Flavor: {self._flavor.name}, Total Price: ${self.get_total()}"
    
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
        return sum(drink.get_total() for drink in self._items)

    def get_num_items(self):
        return len(self._items)

    def get_tax(self):
        return self.get_total() * self._tax_rate

    def get_receipt(self):
        """generates a receipt for the order."""
        receipt_data = {
            "number_drinks": self.get_num_items(),
            "drinks": [],
            "subtotal": self.get_total(),
            "tax": self.get_tax(),
            "grand_total": self.get_total() + self.get_tax()
        }

        for drink in self._items:
            drink_data = {
                "base": drink.get_base().value, 
                "size": drink._size.value, 
                "flavors": [flavor.value for flavor in drink.get_flavors()],
                "total_cost": drink.get_total() 
            }
            receipt_data["drinks"].append(drink_data)
        return receipt_data

    def add_item(self, item):
        if isinstance(item, (Drink, Food)):
            self._items.append(item)
        else:
            raise ValueError("You can only add drinks or food to this order.")

    def remove_item(self, index):
        if 0 <= index < len(self._items):
            self._items.pop(index)
        else:
            raise IndexError("Invalid index, cannot remove item.")
        
        
        
    
        
    
    
    
    
    