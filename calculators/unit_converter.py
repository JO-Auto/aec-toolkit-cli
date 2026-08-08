import sys


def meter_to_feet(meters):
    feet = meters * 3.28084
    return feet


def feet_to_meter(feet):
    meter = feet * 0.3048
    return meter


def millimeters_to_meter(millimeters):
    meter = millimeters * 0.001
    return meter


def meters_to_millimeters(meters):
    millimeters = meters * 1000
    return millimeters


def unit_converter():
    print("=============================")
    print("       Unit Converter       ")
    print("=============================")

    conversion = int(input(
        "Press the number respective to the conversion you want\n"
        "1. Meters → Feet\n"
        "2. Feet → Meters\n"
        "3. Millimeters → Meters\n"
        "4. Meters → Millimeters\n"
        "5. Back\n"
    ))

    if conversion == 5:
        sys.exit()

    number = float(input("What is the number do you like to convert? "))

    if conversion == 1:
        print(meter_to_feet(number))
    elif conversion == 2:
        print(feet_to_meter(number))
    elif conversion == 3:
        print(millimeters_to_meter(number))
    elif conversion == 4:
        print(meters_to_millimeters(number))


unit_converter()
