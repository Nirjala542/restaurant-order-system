
# define the menu of restaurant
menu = {
'pizza':40,
'burger':30,
'salad':40,
'coffee':50,
'dosa':100,
'tea':40,
}

print("welcome to the sharma restaurant")
print("menu")
print("pizza:Rs40 \nburger:Rs30\nsalad:Rs40\ncoffee:Rs50\ndosa:Rs100\ntea:Rs40\n ")
order_total=0
while True:
    item_1=input("Hlo,please enter the name of the item you want to order: ").lower()
    if item_1 in menu:
       order_total+=menu[item_1]
       print(f"your item {item_1} is confirmed")
    else:
       print(f"your item {item_1} is not in our restaurant")

    another_order=input("Do you want to add another item (yes/no)").lower()
    if another_order.lower()!="yes":
       break
print("Thank you for visiting 😊")
 
print(f"total amount of item to pay{order_total}: ")
        