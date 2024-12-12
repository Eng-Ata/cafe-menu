class Items:
    def __init__(self):
        self.cost = [80000, 70000, 75000, 60000, 70000, 90000, 85000, 20000, 50000, 30000]
        self.products = ["Latte", "Flat White", "Americano", "Espresso", "Cake", "Nutella Cake",
                         "Lemon Pie", "Black Tea", "Matcha", "Saffron Tea"]

class Order:
    def __init__(self, item, number, items):
        self.total_cost = items.cost[item - 1] * number
        print(f"You want {number} {items.products[item - 1]} and total cost of that is: {self.total_cost}T")

def menu():
    print("☕✨🍩✨🍪✨🍵✨🍹✨🧋✨🍸 MENU ☕✨🍩✨🍪✨🍵✨🍹✨🧋✨🍸 ")
    print("COFFEE.....................")
    print(f" 1- Latte              80'000 T")
    print(f" 2- Flat White         70'000 T")
    print(f" 3- Americano          75'000 T")
    print(f" 4- Espresso           60'000 T")
    print("DESSERTS & CAKES..........")
    print(f" 5- Cake               70'000 T")
    print(f" 6- Nutella Cake       90'000 T")
    print(f" 7- Lemon Pie          85'000 T")
    print("TEA........................")
    print(f" 8- Black Tea          20'000 T")
    print(f" 9- Matcha             50'000 T")
    print(f"10- Saffron Tea        30'000 T")

def main():
    items = Items()
    total_cost = 0
    menu()

    while True:
        try:
            item = int(input("Enter the item number you want😊: "))
            number = int(input("How many do you want😃? "))

            if item < 1 or item > len(items.products):
                print("Invalid item number. Please try again.")
                continue

            order = Order(item, number, items)
            total_cost += order.total_cost

            is_more = input("Do you have another order🤔? (y/n): ").strip().lower()
            if is_more != 'y':
                break
        except ValueError:
            print("Invalid input. Please enter numeric values.")

    print(f"Your total payment is: {total_cost}T")

if __name__ == "__main__":
    main()
