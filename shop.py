class product:
    def __init__(self,name,quantity) -> None:
        self.name=name
        self.quantity=quantity
    def __str__(self) -> str:
        return f"product:{self.name}, quantity:{self.quantity}"
class Shop:
    def __init__(self) -> None:
        self.products={}

    def add_product(self,product):
        if product.name in self.products:
            self.products[product.name]+=product.quantity
        else:
            self.products[product.name]=product.quentity

    def buy_product(self,product_name,quantity):
        if product_name is not self.products:
            return "product not available."
        if self.products[product_name]<quantity:
            return f"Insufficient stock. Only {self.products[product_name]} unit of {product_name} are availavle. "
        self.products[product_name]-=quantity
        return f"Congratulations! You successfully purchased {quantity} of {product_name}."
    
    def display_inventoty(self):
        if not self.products:
            print("The shop is currently empty.")
        else:
            print("Available Products:")
            for product_name, quantity in self.products.items():
                print(f"- {product_name} (Quantity: {quantity})")

        
shop=Shop()
while True:
    print("\nShop Menu:")
    print("1. Add Product")
    print("2. Buy Product")
    print("3. View Inventory")
    print("4. Exit") 

    choice=input("Enter your choice (1-4): ")

    if choice == "1":
        product_name = input("Enter product name: ")
        try:
            quantity = int(input("Enter quantity to add: "))
            if quantity < 0:
                raise ValueError("Quantity cannot be negative.")
            shop.add_product(product(product_name, quantity))
            print(f"{quantity} units of {product_name} added successfully!")
        except ValueError as e:
            print("Invalid input:", e)
    elif choice == "2":
        product_name = input("Enter product name to buy: ")
        try:
            quantity = int(input("Enter quantity to buy: "))
            if quantity < 0:
                raise ValueError("Quantity cannot be negative.")
            print(shop.buy_product(product_name, quantity))
        except ValueError as e:
            print("Invalid input:", e)

    elif choice == "3":
        shop.display_inventory()

    elif choice == "4":
        print("Exiting the shop.")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")

    