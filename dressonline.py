
collection = { "fromal shirt" : 1200,
              "casual shirt"  : 800,
              "tshirt"       : 700,
              "under wear"    : 500,
              "vest"          : 500,
              "coatsuit"      : 5000,
              "formal pants"  : 900,
              "casual pants"  : 700,
              "track pants"   : 650
               
}

cart = []
total = 0
print("----------MENU----------")
for key,value in collection.items():
    print(f"{key:15} : ₹ {value}")
print("------------------------")


while True:
    purchase = input("Select the  item u need to purchase (q to quit) :")

    if purchase.lower() == "q":
        break
    elif collection.get(purchase) is not None:
        cart.append(purchase)
print("-----------Your order------------")
for purchase in cart:
    total += collection.get(purchase)
    print(purchase,end="")

print()
print(f"Your total is : ₹{total:2f}")
print("---------------------------------")