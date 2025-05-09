foods=[]
prices=[]
total=0

while True:
    food =input("ENTER A FOOD TO BUY(press q or Q to exit) :")
    if food.lower()=="q":
        print("you exited successfully!")
        break
    else:
        price=int(input(f"ENTER THE PRICE OF A FOOD {food}: $"))
        foods.append(food)
        prices.append(price)

print("----YOUR CART----")

for food in foods:
    print(f"{food}-->${price}")

total=sum(prices)
print(f"TOTAL PRICE ${total}")