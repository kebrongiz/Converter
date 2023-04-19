def converter():
    choice = input(
        "Enter the conversion you'd like to perform (1 for kg to lbs, 2 for miles to km, 3 for hours to minutes): ")

    while choice != "1" and choice != "2" and choice != "3":
        print("invalid input")
        choice = input(
            "Enter the conversion you'd like to perform (1 for kg to lbs, 2 for miles to km, 3 for hours to minutes): ")

    if choice == "1":
        kg = float(input("Enter weight in kilograms: "))
        pounds = round((kg * 2.20462), 4)
        print("{} kilogrmas = {} pounds".format(kg, pounds))
    if choice == "2":
        mi = float(input("Enter length in miles: "))
        km = round((mi * 1.60934), 4)
        print("{} Miles = {} Kilometers".format(mi, km))
    if choice == "3":
        hr = float(input("Enter time in hours: "))
        min = round((hr * 60), 2)
        print("{} hours = {} minutes".format(hr, min))


converter()
