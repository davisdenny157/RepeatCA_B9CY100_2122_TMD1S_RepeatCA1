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
    
    def value(self):
        """
        This function calculates the value of total price 
        """

        sum = 0

        for i in self.items:
          print(f"{i['item']} : {i['total_price']}")
          sum += i['total_price']

        print(f"Total Price is {sum}")

    def display_items(self):
        """"
        Displays all the items in the basket
        """
        for i in self.items:
          print(f"{i['item']} : {i['total_price']}")