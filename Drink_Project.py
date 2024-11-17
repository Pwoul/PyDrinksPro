class Drink:
    #List of valid bases and flavors for the drinks.
    _valid_bases = {"water", "sprite", "pokecola", "Mr.Salt", "hill fog", "leaf wine"}
    _valid_flavors = {"lemon", "cherry", "strawberry", "mint", "blueberry", "line"}
    
    def __init__(self):
        #initializing a drink without base and an empty list of flavors.
        self._base = None
        self._flavors = set()
        
    def get_base(self):
        return self._base  #returns the drink base.
    
    def get_flavors(self):
        return list(self._flavors)  #returns flavors that are added to the drink.
    
    def get_num_flavors(self):
        return len(self._flavors)  #returns the number of different flavors added to the drink.
    
    def set_base(self, base):
        if base in self._valid_bases:  #validates if a given base is valid.
            self._base = base  #sets the base if valid.
        else:
            #raises an error if the base isn't valid.
            raise ValueError(f"pick a proper base from {self._valid_bases}.")  
        
    def add_flavor(self, flavor):
        #checks and adds flavor if flavor is included in the list of flavors.
        if flavor in self._valid_flavors:
            self._flavors.add(flavor)
        else:
            #raises an error if a given flover isn't included in the list.
            raise ValueError(f"pick a proper flavor from {self._valid_flavors}.")
        
    def set_flavors(self, flavors):
        #sets multiple flavers at once making sure they are all valid/included in the list of flavors.
        for flavor in flavors:  #iterates through the given flavors.
            if flavor not in self._valid_flavors:
                #raises an error if a given flover isn't included in the list.
                raise ValueError(f"pick a proper flavor from {self._valid_flavors}.")
        self._flavors = set(flavors)  #updates the flovers set with the new valid flavors.
        
class Order:
    def __init__(self):
        self._items = []  #stores the drinks in order.
        
    def get_items(self):
        return self._items  #returns the list of drinks in an order.
    
    def get_total(self):
        return len(self._items)  #returns and counts the items in an order.
    
    def get_receipt(self):
        receipt = "your order receipt:\n"  #generates reciept.
        for i, drink in enumerate(self._items):  #loops through each drnks in an the order.
            base = drink.get_base()  #gets the drink base.
            flavors = ", ".join(drink.get_flavors())  #get flavors and add to the string.
            #adds the drnks detail to the receipt and returns the receipt.
            receipt += f"{i + 1}: base - {base}, flavors - {flavors}\n"
        return receipt
    
    def add_item(self, drink):
        if isinstance(drink, Drink):  #checks if a drink instace
            self._items.append(drink)  #adds drink to the order.
        else:
            #raises an error if the item added isn't a drink.
            raise ValueError("you can only get drinks from this order")
        
    def remove_item(self, index): #removes the drink from the order by its index.
        if 0 <= index < len(self._items):  #checks if index is valid.
            self._items.pop(index)  #removes the drink from a given index.
        else:
            #raises an error if index is not valid.
            raise IndexError("Invalid, can not remove")
        
        
        
        
    
        
    
    
    
    
    