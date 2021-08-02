import pymysql


host = "127.0.0.1"
user = "root"
password = "pass"
database = "store"
port = 33060

# Establish a database connection
connection = pymysql.connect(host=host, user=user, password=password, database=database, port=port)
cursor = connection.cursor()

# A cursor is an object that represents a DB cursor,
# which is used to manage the context of a fetch operation.


def add_product():
    name = input("\nEnter Product Name: "),
    price = float(input("\nEnter Item Price: "))
    val = [name, price]

    sql = "INSERT INTO products (pname,pprice) VALUES (%s,%s)"
    cursor.execute(sql, val)
    return submenu("products")


def view_products():
    for product in products["products"].values():
        print(f"Name: {product['name']}, Price: {product['price']}")
    return submenu("products")


def update_product():
    for product in products["products"]:
        print(f"{product}: {products['products'][product]['name']} ({products['products'][product]['price']})")

    update_productid = input("\nChoose a Product to Update: ")

    for i, field in enumerate(products["products"][update_productid], start=1):
        print(f"{i}: {field}")

    update_field = (int(input("\nChoose a Field to Update: ")))

    products["products"][update_productid][list(products["products"][update_productid])[update_field-1]] = input("\nEnter New Value:")
    print(f'Products {update_productid} {list(products["products"][update_productid])[update_field-1]} changed to: {list(products["products"][update_productid].values())[update_field-1]}')
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

    update_courierid = input("\nChoose a Courier to Update: ")

    for i, field in enumerate(couriers["couriers"][update_courierid], start=1):
        print(f"{i}: {field}")

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


# def update_order_status():
#     # for order in orders["orders"]:
#     #     print(f"OrderID: {order}, Status: {order['status']}")
#     #
#     # update_index = input("\nChoose an Item to Update: ")
#     return submenu("orders")


def amend_order():
    for order in orders["orders"]:
        print("OrderID:", order, "Status:", orders["orders"][order]["status"])

    update_orderid = input("\nChoose an Order to Update: ")

    print()
    for i, field in enumerate(orders["orders"][update_orderid]):
        print(f"{i}: {field}")
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




connection.commit()
cursor.close()
connection.close()