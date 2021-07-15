products = []
couriers = []

try:
    with open('products.txt') as product_list:
        for line in product_list.readlines():
            products.append(line.strip())
    with open('couriers.txt') as couriers_list:
        for line in couriers_list.readlines():
            couriers.append(line.strip())
except Exception as e:
    print('An error occurred: ' + str(e))

# productsMenu = {"Main Menu": 0, "View List": 1, "Add New Entry": 2, "Update Entry": 3, "Delete Entry": 4}
subMenu = {"Main Menu": 0, "View List": 1, "Add New Entry": 2, "Update Entry": 3, "Delete Entry": 4}
mainMenu = {"Products Menu": 1, "Couriers Menu": 2, "Exit": 0, }


def menu(category):
    if category == "products":
        # productsMenu = productsMenu
        file = "products.txt"
        item_list = products

    elif category == "couriers":
        # couriersMenu = couriersMenu
        file = "couriers.txt"
        item_list = couriers

    else:
        print("Problem With Menu Selection"), exit()

    print()
    for key, value in subMenu.items():
        print(f"{str(key)}: {str(value)}")

    while True:
        try:
            with open(file, "w") as entries:
                for item in item_list:
                    entries.write(item + "\n")
        except Exception as ex:
            print('An error occurred with external file: ' + str(ex))

        option = int(input(f"\nChoose an option: "))
        if option == subMenu["Main Menu"]:
            main_menu()

        elif option == subMenu["View List"]:
            print()
            for item in item_list:
                print(item)
            continue

        elif option == subMenu["Add New Entry"]:
            print()
            item_list.append(input("Enter Name: "))
            continue

        elif option == subMenu["Update Entry"]:
            for items in item_list:
                print(f"{items}: {item_list.index(items)}")
            update_index = (int(input("\nChoose an Item Index to Update: ")))
            item_list[update_index] = input("Enter New Name: ")
            continue

        elif option == subMenu["Delete Entry"]:
            print()
            for item in item_list:
                print(f"{item}: {item_list.index(item)}")
            delete_index = (map(int, input("\nChoose an Item to Delete\nFor Multiple Items Use a Comma: ").split(",")))
            for index in sorted(delete_index, reverse=True):
                del item_list[index]
            continue

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
    else: 
        print("\nInvalid input, try again!")
        return main_menu()


main_menu()
