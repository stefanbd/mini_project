couriers = {"couriers": {
                1: {
                    "name": "1carl",
                    "phone": "2222222"},

                2: {
                    "name": "2carl",
                    "phone": "33333333"}
}


    }



def update_courier():
    for courier in couriers["couriers"]:
        print(f"{courier}: {couriers['couriers'][courier]['name']} ({couriers['couriers'][courier]['phone']})")

    update_courierid = int(input("\nChoose a CourierID to Update: "))

    i = 1
    for field in couriers["couriers"][update_courierid]:
        print(f"{field}: {i}")
        i += 1
    update_field = (int(input("\nChoose a Field to Update: ")))

    couriers["couriers"][update_courierid][list(couriers["couriers"][update_courierid])[update_field-1]] = input("\nEnter New Value:")
    print(f'Courier {update_courierid} {list(couriers["couriers"][update_courierid])[update_field-1]} changed to: {list(couriers["couriers"][update_courierid].values())[update_field-1]}')

update_courier()