import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",        
    password="ram1312", 
    database="shop_management"   
)

cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(255),
    quantity INT,
    price_per_item FLOAT,
    total_price FLOAT,
    payment_method VARCHAR(50)
)
""")

class Shop:
    products = {
        1: ("Adhirasam", 30),
        2: ("Special Adhirasam", 45),
        3: ("Murukku", 20),
        4: ("Mullu Murukku", 20),
        5: ("Butter Murukku", 30)
    }

    def __init__(self):
        print("\n📋 MENU CARD")
        for k, v in self.products.items():
            print(f"{k}. {v[0]}, (price = ₹{v[1]})")
        print('-' * 25)

        while True:
            try:
                self.product = int(input("Select product (1-5): "))
                if self.product not in self.products:
                    print("Invalid product number! Please select 1-5 only.")
                    continue
                self.quantity = int(input("Enter quantity: "))
                break
            except ValueError:
                print("Please enter a valid number.")


class Purchase(Shop):
    def price_item(self):
        product, price = self.products[self.product]
        self.total_price = self.quantity * price
        print(f"\nYou selected: {product}")
        print(f"Quantity: {self.quantity}")
        print(f"Price per item: ₹{price}")
        print(f"Total Price: ₹{self.total_price}\n")

        self.order = input("Do you want to cancel the order? (y/n): ").lower()

        if self.order == "y":
            print("Your order is cancelled.")
            return False
        else:
            print("Order confirmed.")
            self.product_name = product
            self.price_per_item = price
            return True


class Transaction:
    def __init__(self, purchase):
        self.purchase = purchase
        while True:
            try:
                print("\nPAYMENT OPTIONS")
                print("1. Cash")
                print("2. Card")
                print("3. UPI")
                choice = int(input("Select payment method (1-3): "))

                if choice == 1:
                    self.payment = "cash"
                elif choice == 2:
                    self.payment = "card"
                elif choice == 3:
                    self.payment = "upi"
                else:
                    print("Invalid choice! Please select 1, 2, or 3.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number (1-3).")

    def payment_method(self):
        print(f"{self.payment.capitalize()} payment successful\nOrder placed successfully!")
        print("-" * 30)

        cursor.execute("""
        INSERT INTO orders (product_name, quantity, price_per_item, total_price, payment_method)
        VALUES (%s, %s, %s, %s, %s)
        """, (self.purchase.product_name, self.purchase.quantity,
              self.purchase.price_per_item, self.purchase.total_price, self.payment))
        db.commit()

        


order = Purchase()
if order.price_item():
    trans = Transaction(order)
    trans.payment_method()


cursor.close()
db.close()
