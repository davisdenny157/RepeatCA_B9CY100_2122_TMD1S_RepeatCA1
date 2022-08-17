class Basket:

    def __init__(self):
        """ Price list is a dictionary containing key as item name and value as price"""
        self.price_list = {
            "Pepsi": 2,
            "Cococola": 2.5,
            "Burger": 25,
            "Sandwich": 30
        }

        """ Item is a list of dictionaries which contains the items in basket """
        self.items = []

    def add_item(self, item_name, quantity):
        """ This class method accepts item name and quantity 
            and stores it in the items variable along with total price """
        try:
          if quantity < 1:
            print("Error: Please enter a positive non zero quantity")
          else:
            price = self.price_list[item_name]
            total_price = price * quantity
            self.items.append({"item": item_name, "total_price": total_price})
        except KeyError as e:
          print("KeyError: ", e)