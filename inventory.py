# ================ The beginning of the class ===============================
""" A class called shoe, which helps a store manager or any other employee
 to:
1. view shoes in stock using shoe code
2. shoes that need restocking/ shoes with the lowest quantity
3. shoes that have the largest quantity and are for sale
4. the price of the shoes in stock
 The use of a text document to import or export the information from or to, is
 used in this task
"""


class Shoe:
    # class constructor to initialize shoe information
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # Shoe methods to return the cost, quantity of the shoes and a string
    # representation of the class
    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return (f"{self.country}, {self.code}, {self.product}, {self.cost}, "
                f"{self.quantity}")


# ================== Shoe list ==========================================
shoe_list = []


# ===================Functions outside the class ========================
# Read shoes from the text inventory.txt file and store them to the shoe list
def read_shoes_data():
    try:
        with open('inventory.txt', 'r') as inFile:
            next(inFile)  # Skip the header line
            for line in inFile:
                line_list = line.strip().split(',')
                shoe_list.append(Shoe(*line_list))
    except FileNotFoundError:
        print("File is not found")


# ----------- View all the shoes in the shoe list - shoe_list --------------
def view_all():
    print("Shoe Details:")
    for i, shoe in enumerate(shoe_list, start=1):
        print(f'{i}. {str(shoe)}')


# search for shoe with the lowest quantity and restock it , update on the file
def re_stock():
    low_quantity_shoe = min(shoe_list, key=lambda x: int(x.quantity))
    print(f"The shoe with lowest quantity in stock: \n{low_quantity_shoe}")
    restock = input("Do you want to restock the shoe? type yes/no: ").lower()

    if restock == 'yes':
        increase_quantity = int(input("Please enter the new quantity: "))
        low_quantity_shoe.quantity += increase_quantity
        print("You have successfully updated the quantity!")

        with open('inventory.txt', 'a') as outFile:
            outFile.write(
                f'\n{low_quantity_shoe.country}, {low_quantity_shoe.code}, '
                f'{low_quantity_shoe.product}, {low_quantity_shoe.cost}, '
                f'{low_quantity_shoe.quantity}')
    elif restock == 'no':
        print("You have decided not to restock the shoe!")
    else:
        print("You have entered invalid option!")


# searching shoe by code and print out the information about the shoe
def search_shoe():
    code = input("Enter code: ")
    for shoe in shoe_list:
        if code == shoe.code:
            print(str(shoe))
            break
    else:
        print("The shoe code was not found!")


# calculate the total value of the shoe in stock
def value_per_item():
    print("Value per Item:")
    for shoe in shoe_list:
        total_value = float(shoe.cost) * int(shoe.quantity)
        print(f'{str(shoe)} has a total value of: {total_value}')


# show the shoe with the highest quantity in stock
def highest_qty():
    high_quantity = max(shoe_list, key=lambda x: int(x.quantity))
    print(f"The shoe with highest quantity is: \n{high_quantity}")
    print("This shoe is for sale!")


# ==================== Main Menu ==============================================
""" Call the function read shoes, and then provide the user with menu with 
options what the user can do """
read_shoes_data()

while True:
    print("\n====== Main Menu ======")
    print("1. View all shoes")
    print("2. Re-stock a shoe")
    print("3. Search for a shoe by code")
    print("4. Calculate value per item")
    print("5. Find shoe with highest quantity")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        view_all()
    elif choice == '2':
        re_stock()
    elif choice == '3':
        search_shoe()
    elif choice == '4':
        value_per_item()
    elif choice == '5':
        highest_qty()
    elif choice == '6':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 6.")
