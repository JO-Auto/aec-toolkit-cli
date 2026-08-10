def meters_to_feet(meters):
    feet = meters * 3.28084
    return feet


def feet_to_meters(feet):
    meter = feet * 0.3048
    return meter


def millimeters_to_meters(millimeters):
    meter = millimeters * 0.001
    return meter


def meters_to_millimeters(meters):
    millimeters = meters * 1000
    return millimeters


def unit_converter():
    print("==============================")
    print("        Unit Converter        ")
    print("==============================")

    while True:
        try:
            conversion = int(input(
                "1. Meters → Feet\n"
                "2. Feet → Meters\n"
                "3. Millimeters → Meters\n"
                "4. Meters → Millimeters\n"
                "5. Back\n"
                "Press the number respective to the conversion you want: "
            ))

            if not 1 <= conversion <= 5:
                print("Invalid input")
                continue

            if conversion == 5:
                return

        except ValueError:
            print("Invalid input")
            continue

        while True:
            try:
                number = float(input("What is the number do you like to convert? "))

                if number < 0:
                    print("Invalid input")
                    continue

            except ValueError:
                print("Invalid input")
                continue

            if conversion == 1:
                print(f"{round(meters_to_feet(number), 2)} feet")
            elif conversion == 2:
                print(f"{round(feet_to_meters(number), 2)} meters")
            elif conversion == 3:
                print(f"{round(millimeters_to_meters(number), 2)} meters")
            elif conversion == 4:
                print(f"{round(meters_to_millimeters(number), 2)} millimeters")
            break
