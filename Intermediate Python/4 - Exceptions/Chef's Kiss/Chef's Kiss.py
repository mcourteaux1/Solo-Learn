menu = ['Fries', 'Sandwich', 'Cheeseburger', 'Coffee', 'Soda']

order = input()

try:
    print(menu[int(order)])
    print("Thanks for your order")
except:
    print("Item not found")