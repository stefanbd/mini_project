import json
import pprint

products = {"products": {}}
couriers = {"couriers": {}}
orders = {"orders": {}}

try:
    with open('products.json') as products_list:
        products.update(json.load(products_list))   
    with open('couriers.json') as couriers_list:
        couriers.update(json.load(couriers_list))
    with open("orders.json") as orders_list:
        orders.update(json.load(orders_list))

except Exception as e:
    print('An error occurred opening external file: ' + str(e))

menus = {

    "mainMenus": {

        "Products Menu": 1,
        "Couriers Menu": 2,
        "Orders Menu": 3,
        "Exit": 0},


    "subMenus": {

        "productsMenu": {
            "Main Menu": 0,
            "View Products": 1,
            "Add New Product": 2,
            "Update Product": 3,
            "Delete Product": 4},
        
        "couriersMenu": {
            "Main Menu": 0,
            "View Couriers": 1,
            "Add New Courier": 2,
            "Update Courier": 3,
            "Delete Courier": 4},

        "ordersMenu": {
            "Main Menu": 0,
            "View Orders": 1,
            "Create Order": 2,
            "Update Order Status": 3,
            "Amend Order": 4,
            "Delete Order": 5},
    }
}


def mainmenu():
    print()
    for menu, value in menus["mainMenus"].items():
        print(f"{str(menu)}: {str(value)}")
    selection = int(input("\nChoose an option: "))
    if selection == menus["mainMenus"]["Products Menu"]:
        submenu("products")
    if selection == menus["mainMenus"]["Couriers Menu"]:
        submenu("couriers")
    elif selection == menus["mainMenus"]["Orders Menu"]:
        submenu("orders")
    elif selection == menus["mainMenus"]["Exit"]:
        exit()
    else:
        print("\nInvalid input, try again!")
        return mainmenu()


def submenu(category):
    item_list = []
    sub_menu = {}
    file = str()

    if category == "products":
        sub_menu = menus["subMenus"]["ordersMenu"]
        file = "products.json"
        item_list = products

    elif category == "couriers":
        sub_menu = menus["subMenus"]["couriersMenu"]
        file = "couriers.json"
        item_list = couriers
        
    elif category == "orders":
        sub_menu = menus["subMenus"]["ordersMenu"]
        file = "orders.json"
        item_list = orders

    else:
        print("Invalid Menu"), exit()

    print()
    for key, value in sub_menu.items():
        print(f"{str(key)}: {str(value)}")

    while True:
        print()
        try:
            with open(file, "w") as entries:
                json.dump(item_list, entries, indent=4)

        except Exception as ex:
            print('An error occurred writing to external file: ' + str(ex))

        option = int(input(f"\nChoose an option: "))
        if option == sub_menu["Main Menu"]:
            mainmenu()

        elif option == sub_menu["View Couriers"]:
            print()
            for courier in item_list["couriers"]:
                print(f"Name: {courier['name']}, Phone: {courier['mobile']}")
            continue
        
        elif option == sub_menu["View Products"]:
            print()
            for product in item_list["products"]:
                print(f"Name: {product['name']}, Price: {product['price']}")
            continue

        elif option == sub_menu["Add New Courier"]:
            courierid = str(len(item_list["couriers"])+1)
            new_courier = {courierid: {
                "name": input("\nEnter Courier Name: "),
                "phone:": input("\nEnter Courier Mobile: ")
            }
            }
            item_list["couriers"].update(new_courier)
            continue
        
        elif option == sub_menu["Add New Product"]:

            productid = str(len(item_list["couriers"]) + 1)
            new_product = {productid: {
                "name": input("\nEnter Product Name: "),
                "price:": input(float("\nEnter Item Price: "))
            }
            }
            item_list["products"].update(new_product)
            continue

        elif option == sub_menu["Update Courier"]:
            for items in item_list:
                print(f"{items}: {item_list.index(items)}")
            # update_index = (int(input("\nChoose an Item Index to Update: ")))
            item_list[(int(input("\nChoose an Item Index to Update: ")))] = input("Enter New Name: ")
            continue
        
        elif option == sub_menu["Update Product"]:
            continue

        elif option == sub_menu["Delete Courier"]:
            for item in item_list:
                print(f"{item}: {item_list.index(item)}")
            delete_index = (map(int, input("\nChoose an Item to Delete\nFor Multiple Items Use a Comma: ").split(",")))
            for index in sorted(delete_index, reverse=True):
                del item_list[index]
            continue
        
        elif option == sub_menu["Delete Product"]:
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
            for courier in couriers["couriers"]:
                print(f"ID: {courier}, Name: {courier['name']}")
                
            new_order[orderid]["courier"] = couriers["couriers"]["courierid"][int(input("\nSelect Courier: "))]
            new_order[orderid]["status"] = "Preparing"

            item_list["orders"].update(new_order)

            continue
            
        elif option == sub_menu["View Orders"]:
            pprint.pprint(orders, sort_dicts=False)
            
        elif option == sub_menu["Update Order Status"]:
            for order in item_list["orders"]:
                print(f"OrderID: {order}, Status: {order['status']}")

            update_index = input("\nChoose an Item to Update: ")
            
        elif option == sub_menu["Amend Order"]:
            for order in item_list["orders"]:
                print("OrderID:", order, "Status:", orders["orders"][order]["status"])
            
            update_index = input("\nChoose an Order to Update: ")
            for key, value in item_list["orders"][update_index].items():
                print(f"{key}: {value}")
                
            update_field = input("\nChoose a Field to Update: ")
            item_list["orders"][update_index][update_field] = input("\nEnter New Status: ")
        
        elif option == sub_menu["Delete Order"]:
            for order in item_list["orders"]:
                print("Item ID:", order, "Status:", item_list["orders"][order]["status"])

            delete_index = (map(int, input("\nChoose an OrderID to Delete\nFor Multiple Items Use a Comma: ").split(",")))
            for index in sorted(delete_index, reverse=True):
                del item_list["orders"][index]
                
            continue
                
        else:
            print("\nInvalid input, try again!")
            continue


mainmenu()
