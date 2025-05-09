#Concession Stand Program
#practice for dictionary {key:value}

menu={"PIZZA":3.00,
      "NACHOS":1.50,
      "POPCORN":4.00,
      "FRIES":2.50,
      "SODA":3.00,
      "LEMONADE":3.50}

cart=[]
total=0


print("-------MENU-------")
for key,value in menu.items():
    print(f"{key:11}:${value:.2f}")
print("-------------------")

while True:
    food=input("SELECT AN ITEM (q to quit):  \n").upper()

    if food =="Q":
        print()
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("--------YOUR ORDER-----------")
for food in cart:
    total=total+menu.get(food)
    print(food,end=f"-${value}\n")

print()
print(f"Total is ${total:.2f}")

