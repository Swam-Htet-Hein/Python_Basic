price = 250
if price >= 300:
    print(f"You'll get 30% discount!")
    print(f"That will be {price-(price*(30/100))}$")
elif price >= 200 and price < 300:
    print(f"You'll get 20% discount!")
    print(f"That will be {price-(price*(20/100))}$")
elif price >= 100 and price < 200:
    print(f"You'll get 10% discount!")
    print(f"That will be {price-(price*(10/100))}$")
elif price >= 1 and price < 100:
    print(f"You'll get 5% discount!")
    print(f"That will be {price-(price*(5/100))}$")
else:
    print("There will be no discount for you.")