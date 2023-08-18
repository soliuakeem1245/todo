def show_menu():
    print("Welcome to my great App Follow the menu below to access the great features of the app")
    print("4. Add food")
    print("3. Find food")
    print("2. Delete food")
    print("1. Edit food")
    print("0. view all food")


def add_food(food_list):
    food_name = input("Enter the name of the food: ")
    food_list.append(food_name)
    print(f"{food_name} has been added to the food list.")


def find_food(food_list):
    food_name = input("Enter the name of the food: ")
    food_list.append(food_name)
    print(f"{food_name} has been found the in food list.")
