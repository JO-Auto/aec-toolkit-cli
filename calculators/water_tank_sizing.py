def calculate_required_tank_volume(number_people, consumption_per_day, storage_days):
    daily_water_demand = number_people * consumption_per_day
    required_tank_volume = daily_water_demand * storage_days
    cubic_meters = required_tank_volume * 0.001
    return required_tank_volume, cubic_meters


def water_tank_sizing():
    print("==============================")
    print("       Water Tank Sizing       ")
    print("==============================")

    while True:
        try:
            choice = int(input("Press 1 to Continue\n"
                               "Press 2 to Back\n"))
            if not 1 <= choice <= 2:
                print("Invalid input")
                continue

        except ValueError:
            print("Invalid input")
            continue

        if choice == 2:
            return

        while True:
            try:
                number_of_people = int(input("Number of people: "))
                consumption_per_day = float(input("Daily consumption per person (L/person/day): "))
                storage_days = float(input("Storage duration: "))

                if number_of_people <= 0 or consumption_per_day <= 0 or storage_days <= 0:
                    print("Invalid input")
                    continue

            except ValueError:
                print("Invalid input")
                continue

            required_tank_volume, cubic_meters = calculate_required_tank_volume(number_of_people,
                                                                              consumption_per_day,
                                                                              storage_days)

            print(f"{round(required_tank_volume, 2)} L ({round(cubic_meters, 2)}m³)")
            break
