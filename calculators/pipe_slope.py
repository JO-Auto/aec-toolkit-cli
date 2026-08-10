def calculate_slope():
    print("=============================")
    print("      Determining Slope      ")
    print("=============================")

    while True:
        try:
            choice = int(input("Press 1 to Continue\n"
                               "Press 2 to Back\n"))
            if not 1 <= choice <= 2:
                print("Invalid input")
                continue

        except ValueError:
            print("Invalid input")

        else:
            if choice == 2:
                return

            while True:
                try:
                    rise = float(input("What is the rise you want to determine the slope? "))
                    run = float(input("And the run? "))

                except ValueError:
                    print("Invalid input")

                else:
                    slope = (rise / run) * 100
                    print(f"{slope} %")
                    break
