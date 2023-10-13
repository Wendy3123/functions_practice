def eatLunch(list):
    for x in range(len(foods)):
        if len(list) >= 1:
            if x == 0:
                print(f"First I eat {list[0]}")
            else:
                print(f"Then I eat {list[x]}")
    if len(list) == 0:
        print("My lunchbox is empty!")


foods = ['apple', 'bluebery', 'muffin', 'carrot', 'cake']
eatLunch(foods)
