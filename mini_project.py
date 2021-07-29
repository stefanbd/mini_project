import json
import pprint

products = {"products": {}, "pid": 1}
couriers = {"couriers": {}, "cid": 1}
orders = {"orders": {}, "oid": 1}


try:
    with open("products.json") as products_list:
        products.update(json.load(products_list))   
    with open("couriers.json") as couriers_list:
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
            "Main Menu": [0, "mainmenu()"],
            "View Products": [1, "view_products()"],
            "Add New Product": [2, "add_product()"],
            "Update Product": [3, "update_product()"],
            "Delete Product": [4, "delete_product()"]},

        "couriersMenu": {
            "Main Menu": [0, "mainmenu()"],
            "View Couriers": [1, "view_couriers()"],
            "Add New Courier": [2, "add_courier()"],
            "Update Courier": [3, "update_courier()"],
            "Delete Courier": [4, "delete_courier()"]},

        "ordersMenu": {
            "Main Menu": [0, "mainmenu()"],
            "View Orders": [1, "view_orders()"],
            "Create Order": [2, "create_order()"],
            "Update Order Status": [3, "update_order_status()"],
            "Amend Order": [4, "amend_order()"],
            "Delete Order": [5, "delete_order()"]},
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
    item_list = {}
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

    return choose_menu(sub_menu, item_list, file)


def choose_menu(sub_menu, item_list, file):
    try:
        with open(file, "w") as entries:
            json.dump(item_list, entries, indent=4)
    except Exception as ex:
        print('An error occurred writing to external file: ' + str(ex))

    print()
    for key, value in sub_menu.items():
        print(f"{str(key)}: {value[0]}")

    option = int(input(f"\nChoose an option: "))
    print()

    for menu in sub_menu:
        if sub_menu[menu][0] == option:
            return eval(sub_menu[menu][1])


def view_products():
    for product in products["products"].values():
        print(f"Name: {product['name']}, Price: {product['price']}")
    return submenu("products")


def add_product():
    productid = products["pid"]

    new_product = {
        productid: {
            "name": input("\nEnter Product Name: "),
            "price": float(input("\nEnter Item Price: "))}
    }

    products["products"].update(new_product)
    products["pid"] += 1
    return submenu("products")


def update_product():
    for product in products["products"]:
        print(f"{product}: {products['products'][product]['name']} ({products['products'][product]['price']})")

    update_productid = int(input("\nChoose a Product to Update: "))

    i = 1
    for field in products["products"][update_productid]:
        print(f"{field}: {i}")
        i += 1

    update_field = (int(input("\nChoose a Field to Update: ")))

    products["products"][update_productid][list(products["products"][update_productid])[update_field-1]] = input("\nEnter New Value:")
    print(f'Products {update_productid} {list(couriers["products"][update_productid])[update_field-1]} changed to: {list(products["products"][update_productid].values())[update_field-1]}')
    return submenu("products")


def delete_product():
    for product in products["products"]:
        print(f"{products['products'][product]['name']}: {product}")

    delete_index = (map(int, input("\nChoose an Item to Delete\nFor Multiple Items Use a Comma: ").split(",")))

    for index in sorted(delete_index, reverse=True):
        del products["products"][str(index)]
    return submenu("products")


def view_couriers():
    for courier in couriers["couriers"].values():
        print(f"Name: {courier['name']}, Phone: {courier['phone']}")
    return submenu("couriers")


def add_courier():
    courierid = couriers["cid"]

    new_courier = {
        courierid: {
            "name": input("\nEnter Courier Name: "),
            "phone": input("\nEnter Courier Mobile: ")}
    }
    couriers["couriers"].update(new_courier)
    couriers["cid"] += 1
    return submenu("couriers")


def update_courier():
    for courier in couriers["couriers"]:
        print(f"{courier}: {couriers['couriers'][courier]['name']} ({couriers['couriers'][courier]['phone']})")

    update_courierid = int(input("\nChoose a Courier to Update: "))

    i = 1
    for field in couriers["couriers"][update_courierid]:
        print(f"{field}: {i}")
        i += 1

    update_field = (int(input("\nChoose a Field to Update: ")))

    couriers["couriers"][update_courierid][list(couriers["couriers"][update_courierid])[update_field-1]] = input("\nEnter New Value:")
    print(f'Courier {update_courierid} {list(couriers["couriers"][update_courierid])[update_field-1]} changed to: {list(couriers["couriers"][update_courierid].values())[update_field-1]}')
    return submenu("couriers")


def delete_courier():
    for courier in couriers["couriers"]:
        print(f"{couriers['couriers'][courier]['name']}: {courier}")

    delete_index = (map(int, input("\nChoose an Item to Delete\nFor Multiple Items Use a Comma: ").split(",")))

    for index in sorted(delete_index, reverse=True):
        del couriers["couriers"][str(index)]
    return submenu("couriers")


def view_orders():
    pprint.pprint(orders, sort_dicts=False)
    return submenu("orders")


def create_order():
    orderid = orders["oid"]

    new_order = {
        orderid: {
            "customer_name": input("\nEnter Customer Name: "),
            "customer_address": input("\nEnter Customer Address: "),
            "customer_phone": input("\nEnter Customer Phone: "), }
    }
    print()
    for courier in couriers["couriers"]:
        print(f"ID: {courier}, Name: {couriers['couriers'][courier]['name']}")
    new_order[orderid]["courier"] = input("\nSelect CourierID: ")
    new_order[orderid]["status"] = "Preparing"

    orders["orders"].update(new_order)
    orders["oid"] += 1
    return submenu("orders")


def update_order_status():
    # for order in orders["orders"]:
    #     print(f"OrderID: {order}, Status: {order['status']}")
    #
    # update_index = input("\nChoose an Item to Update: ")
    return submenu("orders")


def amend_order():
    for order in orders["orders"]:
        print("OrderID:", order, "Status:", orders["orders"][order]["status"])

    update_orderid = input("\nChoose an Order to Update: ")

    i = 1
    print()
    for field in orders["orders"][update_orderid]:
        print(f"{field}: {i}")
        i += 1

    update_field = int(input("\nChoose a Field to Update: "))

    orders["orders"][update_orderid][list(orders["orders"][update_orderid])[update_field - 1]] = input(
        "\nEnter New Value:")
    print(
        f'Courier {update_orderid} {list(orders["orders"][update_orderid])[update_field - 1]} changed to: {list(orders["orders"][update_orderid].values())[update_field - 1]}')
    return submenu("orders")


def delete_order():
    for order in orders["orders"]:
        print("Item ID:", order, "Status:", orders["orders"][order]["status"])

    delete_index = (map(int, input("\nChoose an OrderID to Delete\nFor Multiple Orders Use a Comma: ").split(",")))
    for index in sorted(delete_index, reverse=True):
        del orders["orders"][str(index)]
    return submenu("orders")


mainmenu()
