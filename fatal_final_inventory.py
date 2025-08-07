# inventory_manager.py

import json
import datetime
import os
import uuid

class Product:
    def __init__(self, name, price, quantity):
        self.id = str(uuid.uuid4())
        self.name = name
        self.price = price
        self.quantity = quantity

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity
        }

class Inventory:
    def __init__(self, filename="inventory.json"):
        self.filename = filename
        self.products = []
        self.load_inventory()

    def add_product(self, product):
        self.products.append(product)
        self.save_inventory()

    def remove_product(self, product_id):
        self.products = [p for p in self.products if p.id != product_id]
        self.save_inventory()

    def list_products(self):
        for product in self.products:
            print(f"{product.name} - ${product.price} x {product.quantity} (ID: {product.id})")

    def save_inventory(self):
        data = [p.to_dict() for p in self.products]
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)

    def load_inventory(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                try:
                    data = json.load(f)
                    self.products = [Product(**p) for p in data]
                except Exception as e:
                    print("Failed to load inventory:", e)

def main():
    inventory = Inventory()

    while True:
        print("\nInventory Manager")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. List Products")
        print("4. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            name = input("Product name: ")
            price = float(input("Price: "))
            quantity = int(input("Quantity: "))
            product = Product(name, price, quantity)
            inventory.add_product(product)
            print("Product added.")
        elif choice == "2":
            product_id = input("Enter Product ID to remove: ")
            inventory.remove_product(product_id)
            print("Product removed.")
        elif choice == "3":
            inventory.list_products()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
