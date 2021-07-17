import json

products = []
couriers = []
orders = {}

try:
    with open('products.txt') as product_list:
        for line in product_list.readlines():
            products.append(line.strip())
    with open('couriers.txt') as couriers_list:
        for line in couriers_list.readlines():
            couriers.append(line.strip())
    with open("orders.json") as orders_list:
        orders = json.load(orders_list)
except Exception as e:
    print('An error occurred: ' + str(e))

ordersMenu = {"Main Menu": 0, "View Orders": 1, "Create Order": 2, "Update Order Status": 3, "Amend Order": 4, "Delete Order": 5}
productsMenu = {"Main Menu": 0, "View Products": 1, "Add New Product": 2, "Update Product": 3, "Delete Product": 4}
couriersMenu = {"Main Menu": 0, "View Couriers": 1, "Add New Courier": 2, "Update Courier": 3, "Delete Courier": 4}
mainMenu = {"Products Menu": 1, "Couriers Menu": 2, "Orders Menu": 3, "Exit": 0, }


def menu(category):
    if category == "products":
        sub_menu = productsMenu
        file = "products.txt"
        item_list = products

    elif category == "couriers":
        sub_menu = couriersMenu
        file = "couriers.txt"
        item_list = couriers
        
    elif category == "orders":
        sub_menu = ordersMenu
        file = "orders.json"
        item_list = orders

    else:
        print("Problem With Menu Selection"), exit()

    print()
    for key, value in sub_menu.items():
        print(f"{str(key)}: {str(value)}")

    while True:
        try:
            with open(file, "w") as entries:
                for item in item_list:
                    entries.write(item + "\n")
                json.dump(orders, entries, indent=4)
                
        except Exception as ex:
            print('An error occurred with external file: ' + str(ex))

        option = int(input(f"\nChoose an option: "))
        if option == sub_menu["Main Menu"]:
            main_menu()

        elif option == sub_menu["View Couriers"] or option == sub_menu["View Products"]:
            print()
            for item in item_list:
                print(item)
            continue

        elif option == sub_menu["Add New Courier"] or option == sub_menu["Add New Product"]:
            print()
            item_list.append(input("Enter Name: "))
            continue

        elif option == sub_menu["Update Courier"] or option == sub_menu["Update Product"]:
            for items in item_list:
                print(f"{items}: {item_list.index(items)}")
            update_index = (int(input("\nChoose an Item Index to Update: ")))
            item_list[update_index] = input("Enter New Name: ")
            continue

        elif option == sub_menu["Delete Courier"] or option == sub_menu["Delete Product"]:
            print()
            for item in item_list:
                print(f"{item}: {item_list.index(item)}")
            delete_index = (map(int, input("\nChoose an Item to Delete\nFor Multiple Items Use a Comma: ").split(",")))
            for index in sorted(delete_index, reverse=True):
                del item_list[index]
            continue
        
        elif option == sub_menu["Create Order"]:
            order = {
                "order": {
                    "customer_name": input("\nEnter Customer Name: "),
                    "customer_address": input("\nEnter Customer Address: "),
                    "customer_phone": input("\nEnter Customer Phone: "),
                }
            }
            for item in couriers:
                print(f"{item}: ", couriers.index(item))
                
            order[order["Courier"]] = couriers[int(input("\nSelect Courier: "))]
            order[order["Status"]] = "Preparing"
            
            orders.update(order)
            
            continue
            
        # elif option == subMenu["View Orders"]:

        else:
            print("\nInvalid input, try again!")
            continue


def main_menu():
    print()
    for key, value in mainMenu.items():
        print(f"{str(key)}: {str(value)}")
    selection = int(input("\nChoose an option: "))
    if selection == mainMenu["Products Menu"]:
        menu("products")
    if selection == mainMenu["Couriers Menu"]:
        menu("couriers")
    elif selection == mainMenu["Exit"]:
        exit()
    elif selection == mainMenu["Orders Menu"]:
        menu("orders")
    else: 
        print("\nInvalid input, try again!")
        return main_menu()


main_menu()
