import pymysql

db = {"products": [("ID", "product_id"), ("NAME", "product_name"), ("PRICE", "product_price")],
      "couriers": [("ID", "courier_id"), ("NAME", "courier_name"), ("PHONE", "courier_phone")],
      "orders": [("ID", "order_id"), ("CUSTOMER NAME", "customer_name"), ("CUSTOMER SURNAME", "customer_surname"),
                 ("CUSTOMER ADDRESS", "customer_address"), ("COURIER", "courier_id"), ("STATUS", "order_status")]}

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
            "View Orders": [1, "view_orders()", {"ID": 1, "Courier": 2, "Status": 3}],
            "Create Order": [2, "create_order()"],
            "Update Order Status": [3, "update_order_status()"],
            "Amend Order": [4, "amend_order()"],
            "Delete Order": [5, "delete_order()"]},
    }
}

connection = pymysql.connect(host="127.0.0.1", user="stefan", password="pass", database="store", port=33060)
cursor = connection.cursor()


def save(sql):
    for item in sql:
        print(item)
        cursor.execute(item)
    connection.commit()


def mainmenu():
    print()
    for menu, value in menus["mainMenus"].items():
        print(f"{str(menu)}: {str(value)}")
    selection = int(input("\nChoose an option: "))
    if selection == menus["mainMenus"]["Products Menu"]:
        return submenu("products")
    if selection == menus["mainMenus"]["Couriers Menu"]:
        return submenu("couriers")
    if selection == menus["mainMenus"]["Orders Menu"]:
        return submenu("orders")
    if selection == menus["mainMenus"]["Exit"]:
        cursor.close()
        connection.close()
        return exit()
    else:
        print("\nInvalid input, try again!")
        return mainmenu()


def submenu(category):
    if category == "products":
        sub_menu = menus["subMenus"]["productsMenu"]
    elif category == "couriers":
        sub_menu = menus["subMenus"]["couriersMenu"]
    elif category == "orders":
        sub_menu = menus["subMenus"]["ordersMenu"]
    else:
        cursor.close()
        connection.close()
        exit()
    return choose_menu(sub_menu)


def choose_menu(sub_menu):
    print()
    for key, value in sub_menu.items():
        print(f"{str(key)}: {value[0]}")

    option = int(input("\nChoose an option: "))
    print()

    for menu in sub_menu:
        if sub_menu[menu][0] == option:
            return eval(sub_menu[menu][1])


def view_products():
    cursor.execute('SELECT * FROM products')
    rows = cursor.fetchall()
    for row in rows:
        print(f'ID: {row[0]} | NAME: {row[1]} | PRICE: {row[2]}')
    return submenu("products")


def add_product():
    name = input("\nEnter Product Name: ")
    price = float(input("\nEnter Item Price: "))
    val = (name, price)

    sql = f"INSERT INTO products (product_name,product_price) VALUES {val}",
    save(sql)
    return submenu("products")


def update_product():
    cursor.execute('SELECT * FROM products')
    rows = cursor.fetchall()
    for row in rows:
        print(f'ID: {row[0]} | NAME: {row[1]} | PRICE: {row[2]}')

    update_productid = int(input("\nChoose a ProductID to Update: "))
    print()

    for index, value in enumerate(db["products"][1:], start=1):
        print(f"{index}: {value[0]}")

    update_field = (int(input("\nChoose a Field to Update: ")))
    print()
    sql = f" UPDATE products SET {db['products'][(update_field)][1]} = '{input('Enter New Value: ')}' WHERE product_id = {update_productid}",
    save(sql)
    return submenu("products")


def delete_product():
    sql = ()

    cursor.execute('SELECT * FROM products')
    rows = cursor.fetchall()
    for row in rows:
        print(f'ID: {row[0]} | NAME: {row[1]} | PRICE: {row[2]}')

    delete_index = (map(int, input("\nChoose a ProductID to Delete\nFor Multiple Items Use a Comma: ").split(",")))

    for index in sorted(delete_index, reverse=True):
        sql += f"DELETE FROM products WHERE product_id = {index}",
    save(sql)
    return submenu("products")


def view_couriers():
    cursor.execute('SELECT * FROM couriers')
    rows = cursor.fetchall()
    for row in rows:
        print(f'ID: {row[0]} | NAME: {row[1]} | PHONE: {row[2]}')
    return submenu("couriers")


def add_courier():
    name = input("\nEnter Courier Name: ")
    phone = input("\nEnter Courier Phone: ")
    val = (name, phone)

    sql = f"INSERT INTO couriers (courier_name, courier_phone) VALUES {val}",
    save(sql)
    return submenu("couriers")


def update_courier():
    cursor.execute('SELECT * FROM couriers')
    rows = cursor.fetchall()
    for row in rows:
        print(f'ID: {row[0]} | NAME: {row[1]} | PHONE: {row[2]}')

    update_courierid = int(input("\nChoose a CourierID to Update: "))
    print()

    for index, value in enumerate(db["couriers"][1:], start=1):
        print(f"{index}: {value[0]}")

    update_field = (int(input("\nChoose a Field to Update: ")))
    print()
    sql = f" UPDATE products SET {db['couriers'][(update_field)][1]} = '{input('Enter New Value: ')}' WHERE courier_id = {update_courierid}",
    save(sql)
    return submenu("couriers")


def delete_courier():
    sql = ()

    cursor.execute('SELECT * FROM couriers')
    rows = cursor.fetchall()
    for row in rows:
        print(f'ID: {row[0]} | NAME: {row[1]} | PHONE: {row[2]}')

    delete_index = (map(int, input("\nChoose a CourierID to Delete\nFor Multiple Items Use a Comma: ").split(",")))

    for index in sorted(delete_index, reverse=True):
        sql += f"DELETE FROM couriers WHERE courier_id = {index}",
        save(sql)
    return submenu("couriers")


def view_orders():
    for key, value in menus["subMenus"]["ordersMenu"]["View Orders"][2].items():
        print(f"{key}: {value}")
    print()
    val = int(input("Sort By: "))
    print()

    if val == menus["subMenus"]["ordersMenu"]["View Orders"][2]["ID"]:
        cursor.execute('SELECT * FROM orders ORDER BY order_id')
        rows = cursor.fetchall()
        for row in rows:
            print(f'ID: {row[0]} | CUSTOMER: {row[1]} {row[2]} | ADDRESS: {row[3]} | COURIER: {row[4]} | STATUS: {row[5]}')
    elif val == menus["subMenus"]["ordersMenu"]["View Orders"][2]["Courier"]:
        cursor.execute('SELECT * FROM orders ORDER BY courier_id')
        rows = cursor.fetchall()
        for row in rows:
            print(
                f'ID: {row[0]} | CUSTOMER: {row[1]} {row[2]} | ADDRESS: {row[3]} | COURIER: {row[4]} | STATUS: {row[5]}')
    elif val == menus["subMenus"]["ordersMenu"]["View Orders"][2]["Status"]:
        cursor.execute('SELECT * FROM orders ORDER BY order_status')
        rows = cursor.fetchall()
        for row in rows:
            print(
                f'ID: {row[0]} | CUSTOMER: {row[1]} {row[2]} | ADDRESS: {row[3]} | COURIER: {row[4]} | STATUS: {row[5]}')
    return submenu("orders")


def create_order():
    customer_name = input("\nEnter Customer Name: ")
    customer_surname = input("\nEnter Customer Surname: ")
    customer_address = input("\nEnter Customer Address: ")

    cursor.execute('SELECT * FROM couriers')
    rows = cursor.fetchall()
    print()
    for row in rows:
        print(f'ID: {row[0]} | NAME: {row[1]} | PHONE: {row[2]}')

    order_courier = int(input("\nEnter Order CourierID: "))
    order_status = "Preparing"

    val = (customer_name, customer_surname, customer_address, order_courier, order_status)
    sql = f"INSERT INTO orders (customer_name, customer_surname, customer_address, courier_id, order_status) VALUES {val}",

    save(sql)
    return submenu("orders")


# def update_order_status():

#     return submenu("orders")


def amend_order():
    cursor.execute('SELECT * FROM orders')
    rows = cursor.fetchall()
    for row in rows:
        print(f'ID: {row[0]} | CUSTOMER: {row[1]} {row[2]} | ADDRESS: {row[3]} | COURIER: {row[4]} | STATUS: {row[5]}')

    update_orderid = int(input("\nChoose an OrderID to Update: "))
    print()

    for index, value in enumerate(db["orders"][1:], start=1):
        print(f"{index}: {value[0]}")

    update_field = (int(input("\nChoose a Field to Update: ")))

    if db['orders'][update_field] == "COURIER":
        print()
        cursor.execute('SELECT * FROM couriers')
        rows = cursor.fetchall()
        for row in rows:
            print(f'ID: {row[0]} | NAME: {row[1]} | PHONE: {row[2]}')

        sql = f" UPDATE orders SET {db['orders'][(update_field)][1]} = '{input('Enter New Courier: ')}' WHERE order_id = {update_orderid}",
    else:
        sql = f" UPDATE orders SET {db['orders'][(update_field)][1]} = '{input('Enter New Value: ')}' WHERE order_id = {update_orderid}",

    save(sql)
    return submenu("orders")



def delete_order():
    sql = ()

    cursor.execute('SELECT * FROM orders')
    rows = cursor.fetchall()
    for row in rows:
        print(f'ID: {row[0]} | CUSTOMER: {row[1]} {row[2]} | ADDRESS: {row[3]} | COURIER: {row[4]} | STATUS: {row[5]}')

    delete_index = (map(int, input("\nChoose an OrderID to Delete\nFor Multiple Items Use a Comma: ").split(",")))

    for index in sorted(delete_index, reverse=True):
        sql += f"DELETE FROM orders WHERE order_id = {index}",
        save(sql)
    return submenu("orders")



mainmenu()