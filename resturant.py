# 1).Add food items to Menu
# 2.Show all food items
# 3.Update a Food Item
# 4.Delete a food Item
# 5.Search a food item and display its details
class Resturant:
    def __init__(self):
        self.food_menu=int(input("Enter the food "))
    def add_item(self):
        name=input("Enter the food name:")
        price=int(input("enter the price of the food"))
        self.menu[name]= price
        print("food item added the menu")
    def show_menu(self):
        if not self.food_menu:
            print("the menu is not visible")
        else:
            print("menu:")

    def update_item(self):
        name = input("Enter food item name to update: ")
        if name in self.menu:
            price = float(input("Enter new price: "))
            self.menu[name] = price
            print(f"Food item updated.")
        else:
            print(f"Food item not found.")

    def delete_item(self):
        name = input("Enter food item name to delete: ")
        if name in self.food_menu:
            del self.food_menu[name]
            print(f"Food item deleted.")
        else:
            print(f"Food item not found.")

    def search_item(self):
        name = input("Enter food item name to search: ")
        if name in self.food_menu:
            print(f"Food item")
        else:
            print(f"Food item  not found")
    def main():
        resturant=Resturant()
l=[]
while(1):
    print("Resturant")
    print("1.Add food item")
    print("2.show all foods")
    print("3.Update")
    print("4.delete")
    print("5.search")
    print("6.Exit")
    ch = int(input("Enter your choice"))
    if ch== "1":
        resturant.add_item()
    elif ch == "2":
        resturant.show_menu()
    elif ch == "3":
        resturant.update_item()
    elif ch == "4":
        resturant.delete_item()
    elif ch == "5":
        resturant.search_item()
    elif ch== "6":
        exit()
        break



