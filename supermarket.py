import csv
import os

def read_products_from_csv(file_path):
    products = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append(row)
    return products

def write_products_to_csv(file_path, products):
    with open(file_path, 'w', newline='') as file:
        fieldnames = products[0].keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(products)

def display_products(products):
    for product in products:
        print(f"{product['ID']}. {product['Name']} - ${product['Price']}")

def add_product(products, new_product):
    products.append(new_product)

def remove_product(products, product_id):
    for product in products:
        if product['ID'] == product_id:
            products.remove(product)
            break

def owner_menu(products):
    while True:
        print("\nOwner Menu:")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. Display Products")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            new_product = {}
            new_product['ID'] = input("Enter product ID: ")
            new_product['Name'] = input("Enter product Name: ")
            new_product['Price'] = input("Enter product Price: ")
            add_product(products, new_product)
            write_products_to_csv('products.csv', products)
            print("Product added successfully!")

        elif choice == '2':
            product_id = input("Enter product ID to remove: ")
            remove_product(products, product_id)
            write_products_to_csv('products.csv', products)
            print("Product removed successfully!")

        elif choice == '3':
            display_products(products)

        elif choice == '4':
            break

        else:
            print("Invalid choice. Please try again.")

def customer_menu(products):
    cart = []
    total_products = 0
    total_amount = 0

    while True:
        print("\nCustomer Menu:")
        print("1. Display Products")
        print("2. Add to Cart")
        print("3. Display Cart")
        print("4. Checkout")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            display_products(products)

        elif choice == '2':
            product_id = input("Enter product ID to add to cart: ")
            for product in products:
                if product['ID'] == product_id:
                    cart.append(product)
                    total_products += 1
                    total_amount += float(product['Price'])
                    print("Product added to cart!")

        elif choice == '3':
            print("\nCart:")
            for item in cart:
                print(f"{item['Name']} - ${item['Price']}")
            print(f"Total Products in Cart: {total_products}")
            print(f"Total Amount in Cart: ${total_amount}")

        elif choice == '4':
            print("\nCheckout:")
            print(f"Total Products in Cart: {total_products}")
            print(f"Total Amount in Cart: ${total_amount}")
            print("Thank you for shopping with us!")
            break

        elif choice == '5':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    while True:
        user_type = input("Are you an owner or a customer? Enter '1' for owner or '2' for customer: ")

        if user_type == '1':
            products = read_products_from_csv('products.csv')
            while True:
                owner_menu(products)
                choice = input("Do you want to perform another operation as an owner? (yes/no): ")
                if choice.lower() != 'yes':
                    break  # Exit loop if the owner wants to exit
            break  # Exit loop if a valid choice is made

        elif user_type == '2':
            products = read_products_from_csv('products.csv')
            while True:
                customer_menu(products)
                choice = input("Do you want to perform another operation as a customer? (yes/no): ")
                if choice.lower() != 'yes':
                    break  # Exit loop if the customer wants to exit
            break  # Exit loop if a valid choice is made

        else:
            print("Invalid input. Please enter '1' for owner or '2' for customer.")