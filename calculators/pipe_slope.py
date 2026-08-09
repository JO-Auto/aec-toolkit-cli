def calculate_slope():
    print("=============================")
    print("      Determining Slope      ")
    print("=============================")

    choice = int(input("Press 1 to Continue\n"
                              "Press 2 to Back\n"))
    if choice == 2:
        return

    rise = float(input("What is the rise you want to determine the slope? "))
    run = float(input("And the run? "))

    slope = (rise / run) * 100
    print(f"{slope} %")
