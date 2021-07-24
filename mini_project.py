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
        return submenu("products")
    if selection == menus["mainMenus"]["Couriers Menu"]:
        return submenu("couriers")
    elif selection == menus["mainMenus"]["Orders Menu"]:
        return submenu("orders")
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
        sub_menu = menus["subMenus"]["productsMenu"]
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

    choose_sub_menu(sub_menu, item_list, file)


def choose_sub_menu(sub_menu, item_list, file):

    try:
        with open(file, "w") as entries:
            json.dump(item_list, entries, indent=4)
    except Exception as ex:
        print('An error occurred writing to external file: ' + str(ex))

    print()
    for key, value in sub_menu.items():
        print(f"{str(key)}: {str(value)}")

    option = int(input(f"\nChoose an option: "))

    for menu in sub_menu:
        if sub_menu.get(menu(0)) == option:
            sub_menu[menu][option](1)

    # if option == sub_menu["Main Menu"]:
    #     mainmenu()
    # elif option == sub_menu["View Couriers"]:
    #     view_couriers()
    # elif option == sub_menu["View Products"]:
    #     view_products()
    # elif option == sub_menu["Add New Courier"]:
    #     add_courier()
    # elif option == sub_menu["Add New Product"]:
    #     add_product()
    # elif option == sub_menu["Update Courier"]:
    #     update_courier()
    # # elif option == sub_menu["Update Product"]:
    # #     update_product()
    # elif option == sub_menu["Delete Courier"]:
    #     delete_courier()
    # # elif option == sub_menu["Delete Product"]:
    # #     delete_product()
    # elif option == sub_menu["Create Order"]:
    #     create_order()
    # elif option == sub_menu["View Orders"]:
    #     view_orders()
    # elif option == sub_menu["Update Order Status"]:
    #     update_order_status()
    # elif option == sub_menu["Amend Order"]:
    #     amend_order()
    # elif option == sub_menu["Delete Order"]:
    #     delete_order()
    # else:
    #     print("\nInvalid input, try again!")


def view_couriers():
    for courier in couriers["couriers"]:
        print(f"Name: {courier['name']}, Phone: {courier['mobile']}")
        return submenu("couriers")


def view_products():
    for product in products["products"]:
        print(f"Name: {product['name']}, Price: {product['price']}")
        return submenu("products")


def add_courier():
    courierid = str(len(couriers["couriers"])+1)
    new_courier = {courierid: {
        "name": input("\nEnter Courier Name: "),
        "phone:": input("\nEnter Courier Mobile: ")}
    }
    couriers["couriers"].update(new_courier)
    return submenu("couriers")


def add_product():
    productid = str(len(products["products"]) + 1)
    new_product = {productid: {
        "name": input("\nEnter Product Name: "),
        "price:": input(float("\nEnter Item Price: "))}
    }
    products["products"].update(new_product)
    return submenu("products")


def update_courier():
    for courier in couriers["couriers"]:
        print(f"{courier}: {courier.index(courier)}")
    update_index = (int(input("\nChoose an Item Index to Update: ")))
    couriers[(int(input("\nChoose a CourierID to Update: ")))] = input("Enter New Name: ")
    return submenu("couriers")


def delete_courier():
    for courier in couriers:
        print(f"{courier}: {couriers.index(courier)}")
    delete_index = (map(int, input("\nChoose an Item to Delete\nFor Multiple Items Use a Comma: ").split(",")))
    for index in sorted(delete_index, reverse=True):
        del couriers[index]
    return submenu("couriers")


def create_order():
    orderid = str(len(orders["orders"])+1).zfill(5)

    new_order = {
                orderid: {
                    "customer_name": input("\nEnter Customer Name: "),
                    "customer_address": input("\nEnter Customer Address: "),
                    "customer_phone": input("\nEnter Customer Phone: "), }
    }
    print()
    for courier in couriers["couriers"]:
        print(f"ID: {courier}, Name: {courier['name']}")
    new_order[orderid]["courier"] = couriers["couriers"]["courierid"][int(input("\nSelect Courier: "))]
    new_order[orderid]["status"] = "Preparing"

    orders["orders"].update(new_order)
    return submenu("orders")


def view_orders():
    pprint.pprint(orders, sort_dicts=False)
    return submenu("orders")


def update_order_status():
    for order in orders["orders"]:
        print(f"OrderID: {order}, Status: {order['status']}")

    update_index = input("\nChoose an Item to Update: ")
    return submenu("orders")


def amend_order():
    for order in orders["orders"]:
        print("OrderID:", order, "Status:", orders["orders"][order]["status"])

    update_index = input("\nChoose an Order to Update: ")
    for key, value in orders["orders"][update_index].items():
        print(f"{key}: {value}")

    update_field = input("\nChoose a Field to Update: ")
    orders["orders"][update_index][update_field] = input("\nEnter New Status: ")
    return submenu("orders")


def delete_order():
    for order in orders["orders"]:
        print("Item ID:", order, "Status:", orders["orders"][order]["status"])

    delete_index = (map(int, input("\nChoose an OrderID to Delete\nFor Multiple Orders Use a Comma: ").split(",")))
    for index in sorted(delete_index, reverse=True):
        del orders["orders"][index]
    return submenu("orders")


mainmenu()
