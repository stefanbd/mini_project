import json
import pprint

products = []
couriers = []
orders = {"orders": []}

try:
    with open('products.txt') as product_list:
        for line in product_list.readlines():
            products.append(line.strip())
    with open('couriers.txt') as couriers_list:
        for line in couriers_list.readlines():
            couriers.append(line.strip())
    with open("orders.json") as orders_list:
        orders.update(json.load(orders_list))

except Exception as e:
    print('An error occurred: ' + str(e))

subMenu = {"menu": {
    "ordersMenu": {"Main Menu": 0, "View Orders": 1, "Create Order": 2, "Update Order Status": 3, "Amend Order": 4, "Delete Order": 5},
    "productsMenu": {"Main Menu": 0, "View Products": 1, "Add New Product": 2, "Update Product": 3, "Delete Product": 4},
    "couriersMenu": {"Main Menu": 0, "View Couriers": 1, "Add New Courier": 2, "Update Courier": 3, "Delete Courier": 4},
    }
}
mainMenu = {"Products Menu": 1, "Couriers Menu": 2, "Orders Menu": 3, "Exit": 0}


def menu(category):
    item_list = []
    sub_menu = {}
    file = ""

    if category == "products":
        sub_menu = subMenu["menu"]["ordersMenu"]
        file = "products.txt"
        item_list = products

    elif category == "couriers":
        sub_menu = subMenu["menu"]["couriersMenu"]
        file = "couriers.txt"
        item_list = couriers
        
    elif category == "orders":
        sub_menu = subMenu["menu"]["ordersMenu"]
        file = "orders.json"
        # item_list = orders

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
            print('An error occurred writing to external file: ' + str(ex))

        option = int(input(f"\nChoose an option: "))
        if option == sub_menu["Main Menu"]:
            main_menu()

        elif option == sub_menu.get("View Couriers", -0) | option == sub_menu.get("View Products", -0):
            print()
            for item in item_list:
                print(item)
            continue

        elif option == sub_menu.get("Add New Courier", -0) | option == sub_menu.get("Add New Product", -0):
            print()
            item_list.append(input("Enter Name: "))
            continue

        elif option == sub_menu.get("Update Courier", -0) | option == sub_menu.get("Update Product", -0):
            for items in item_list:
                print(f"{items}: {item_list.index(items)}")
            # update_index = (int(input("\nChoose an Item Index to Update: ")))
            item_list[(int(input("\nChoose an Item Index to Update: ")))] = input("Enter New Name: ")
            continue

        elif option == sub_menu.get("Delete Courier", -0) or option == sub_menu.get("Delete Product", -0):
            print()
            for item in item_list:
                print(f"{item}: {item_list.index(item)}")
            delete_index = (map(int, input("\nChoose an Item to Delete\nFor Multiple Items Use a Comma: ").split(",")))
            for index in sorted(delete_index, reverse=True):
                del item_list[index]
            continue
        
        elif option == sub_menu["Create Order"]:
            orderid = str(len(orders["orders"])+1).zfill(5)

            new_order = {
                        orderid: {
                            "customer_name": input("\nEnter Customer Name: "),
                            "customer_address": input("\nEnter Customer Address: "),
                            "customer_phone": input("\nEnter Customer Phone: "),
                        }
            }
            
            print()
            for item in couriers:
                print(f"{item}:", couriers.index(item))
                
            new_order[orderid]["courier"] = couriers[int(input("\nSelect Courier: "))]
            new_order[orderid]["status"] = "Preparing"

            orders["orders"].append(new_order)

            continue
            
        elif option == sub_menu["View Orders"]:
            pprint.pprint(orders, sort_dicts=False)
            
        elif option == sub_menu["Update Order Status"]:
            for order in orders["orders"]:
                print("Order ID: ", order["order_id"])
            
            print()

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
