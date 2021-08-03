import pymysql

db = {"products": [("ID", "product_id"), ("NAME", "product_name"), ("PRICE", "product_price")],
      "couriers": [("ID", "courier_id"), ("NAME", "courier_name"), ("PHONE", "courier_phone")],
      "orders": [("ID", "order_id"), ("CUSTOMER NAME", "customer_name"), ("CUSTOMER SURNAME", "customer_surname"),
                 ("CUSTOMER ADDRESS", "customer_address"), ("COURIER", "courier_id"), ("STATUS", "order_status")]}

host = "127.0.0.1"
user = "stefan"
password = "pass"
database = "store"
port = 33060


connection = pymysql.connect(host=host, user=user, password=password, database=database, port=port)
cursor = connection.cursor()

# #
# # cursor.execute('SELECT * FROM products')
# # rows = cursor.fetchall()
# # for row in rows:
# #     print(f'ID: {row[0]} NAME: {row[1]} PRICE: {row[2]}')
#
#
# for index, value in enumerate(db["products"][1:], start=1):
#     print(f"{index}: {value[0]}")


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
            "View Orders": [{"ID": 1, "Status": 2, "Courier": 3}, "view_orders()"],
            "Create Order": [2, "create_order()"],
            "Update Order Status": [3, "update_order_status()"],
            "Amend Order": [4, "amend_order()"],
            "Delete Order": [5, "delete_order()"]},
    }
}

def view_orders():
    for key, value in menus["subMenus"]["ordersMenu"]["View Orders"][0].items():
        print(f"{value}: {key}")
    print()
    val = int(input("Sort By: "))
    print()

    if val == menus["subMenus"]["ordersMenu"]["View Orders"][0]["ID"]:
        cursor.execute('SELECT * FROM orders ORDER BY order_id')
        rows = cursor.fetchall()
        for row in rows:
            print(f'ID: {row[0]} | CUSTOMER: {row[1]} {row[2]} | ADDRESS: {row[3]} | COURIER: {row[4]} | STATUS: {row[5]}')

    elif val == menus["subMenus"]["ordersMenu"]["View Orders"][0]["Status"]:
        cursor.execute('SELECT * FROM orders ORDER BY order_status')
        rows = cursor.fetchall()
        for row in rows:
            print(
                f'ID: {row[0]} | CUSTOMER: {row[1]} {row[2]} | ADDRESS: {row[3]} | COURIER: {row[4]} | STATUS: {row[5]}')
    elif val == menus["subMenus"]["ordersMenu"]["View Orders"][0]["Courier"]:
        cursor.execute('SELECT * FROM orders ORDER BY courier_id')
        rows = cursor.fetchall()
        for row in rows:
            print(
                f'ID: {row[0]} | CUSTOMER: {row[1]} {row[2]} | ADDRESS: {row[3]} | COURIER: {row[4]} | STATUS: {row[5]}')
        # return submenu("orders")

view_orders()