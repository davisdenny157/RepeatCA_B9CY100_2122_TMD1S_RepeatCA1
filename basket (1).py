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

    