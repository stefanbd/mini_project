couriers = {"couriers": {
                1: {
                    "name": "carl",
                    "phone": "0543534"},

                2: {
                    "name": "carl",
                    "phone": "0543534"}
}


    }



def update_courier():
    for courier in couriers["couriers"]:
        print(f"{courier}: {couriers['couriers'][courier]['name']} ({couriers['couriers'][courier]['phone']})")

    update_courierid = (int(input("\nChoose an CourierID to Update: ")))

    i = 0
    for field in couriers["couriers"][update_courierid]:
        print(f"{field}: {i}")
        i += 1
    update_field = (int(input("\nChoose a Field to Update: ")))

    list(couriers["couriers"][update_field].values())[update_field] = input("\nEnter New Value:")

update_courier()