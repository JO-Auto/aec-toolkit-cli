def calculate_rectangular_volume(length, width, thickness):
    volume = length * width * thickness
    return volume


def material_estimator():
    print("==============================")
    print("      Material Estimator       ")
    print("==============================")

    while True:
        try:
            choice = int(input("Press 1 to Continue\n"
                               "Press 2 to Back\n"))
            if not 1 <= choice <= 2:
                print("Invalid input")
                continue

            if choice == 2:
                return

        except ValueError:
            print("Invalid input")
            continue

        while True:
            try:
                length = float(input("What is the length? "))
                width = float(input("Width? "))
                thickness = float(input("Thickness? "))

                if length <= 0 or width <= 0 or thickness <= 0:
                    print("Invalid input")
                    continue

            except ValueError:
                print("Invalid input")
                continue

            print(round(calculate_rectangular_volume(length, width, thickness), 2))
            break
