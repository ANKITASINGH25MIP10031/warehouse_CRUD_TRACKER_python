# -------------------------------------------
# WAREHOUSE ITEMS CRUD TRACKER
# C - CREATE
# R - READ
# U - UPDATE
# D - DELETE
# -------------------------------------------

warehouse_items = []

# -------------------------------
# CREATE (C)
# -------------------------------
def add_item():
    print("Add a new warehouse item")
    item_name = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    location = input("Enter storage location: ")
    supplier = input("Enter supplier name: ")

    item = {
        "item_name": item_name,
        "quantity": quantity,
        "location": location,
        "supplier": supplier
    }

    warehouse_items.append(item)
    print("Item added successfully!\n")


# -------------------------------
# READ (R)
# -------------------------------
def view_items():
    print("View all warehouse items")
    if not warehouse_items:
        print("No items found.\n")
        return

    for item in warehouse_items:
        print("Item: {}, Quantity: {}, Location: {}, Supplier: {}".format(
            item["item_name"], item["quantity"], item["location"], item["supplier"]
        ))
    print()


# -------------------------------
# UPDATE (U)
# -------------------------------
def update_item():
    print("Update a warehouse item")
    item_name = input("Enter the name of the item to update: ")

    for item in warehouse_items:
        if item["item_name"] == item_name:
            quantity = int(input("Enter new quantity: "))
            location = input("Enter new storage location: ")
            supplier = input("Enter new supplier name: ")

            item["quantity"] = quantity
            item["location"] = location
            item["supplier"] = supplier

            print("Item updated successfully!\n")
            return

    print("Item not found.\n")


# -------------------------------
# DELETE (D)
# -------------------------------
def delete_item():
    print("Delete a warehouse item")
    item_name = input("Enter the name of the item to delete: ")

    for item in warehouse_items:
        if item["item_name"] == item_name:
            confirm = input("Are you sure you want to delete this item? (yes/no): ")
            if confirm.lower() != 'yes':
                print("Deletion cancelled.\n")
            else:
                warehouse_items.remove(item)
                print("Item deleted successfully!\n")
            return

    print("Item not found.\n")


# -------------------------------
# MENU
# -------------------------------
def menu():
    print("------WAREHOUSE ITEM TRACKER (CRUD)------")
    print("1. Add Item (Create)")
    print("2. View Items (Read)")
    print("3. Update Item (Update)")
    print("4. Delete Item (Delete)")
    print("5. Exit")


# -------------------------------
# MAIN LOOP
# -------------------------------
while True:
    menu()
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        add_item()
    elif choice == '2':
        view_items()
    elif choice == '3':
        update_item()
    elif choice == '4':
        delete_item()
    elif choice == '5':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.\n")