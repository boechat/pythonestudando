'''

Write a Python program to create a class representing a shopping cart.
Include methods for adding and removing items, and calculating the total price.

'''

class Shopping_cart:
    def __init__(self):
        self.items = []

    def adding_items(self, item, qtd):
        item_add = (item, qtd)
        print('Adding new Item : ', item, ' ; qtd: ', qtd)
        self.items.append(item_add)

    def removing_itens(self, item):
        for item_rem in self.items:
            if item_rem[0] == item:
                print('Found! Removing Item :', item)
                self.items.remove(item_rem)
                break

    def calculating_total(self):
        total = 0
        for item_total in self.items:
            total += item_total[1]
        return total

#############################################

shopping_cart = Shopping_cart()

shopping_cart.adding_items('Pasta', 50)
shopping_cart.adding_items('Orange', 150)
shopping_cart.adding_items('Apple', 150)
shopping_cart.adding_items('Grape', 250)


print('QTD :', shopping_cart.calculating_total())
print('Items: ', shopping_cart.items)
shopping_cart.removing_itens('Apple')
print('Items: ', shopping_cart.items)
