import os
food_available=["apple","banana","orange", "pizza","burger","grape","milk","egg","steak"]
shopcart = []
while True:
    os.system('cls')
    print("""Choose an Option: 
1. Add an Item
2. View The List
3. Remove and Item
4. Exit""")
    choose = int(input("Choose: "))
    match choose:
        case 1:
            additem = input("Add an item: ")
            if additem in food_available:
                shopcart.append(additem)
                print(f"{additem} is added to the Kart")
                input("Enter to Continue")
            elif additem not in food_available:
                print("Item Not Available")
                input("Enter to Continue")
        case 2:
            print(f"My Food: {shopcart}")
            input("Enter to Continue")
        case 3:
            removeitem= input("Remove an item: ")
            if removeitem in shopcart:
                shopcart.remove(removeitem)
                print(f"{removeitem} have been remove")
                input("Enter to Continue")
            elif removeitem not in shopcart:
                print("Item is not in the List")
                input("Enter to Continue")
        case 4:
            input("Enter To Exit")
            break
        case _:
            print("Error Occurred")
            input("Enter to Continue")