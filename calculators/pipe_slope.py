def calculate_slope(rise, run):
    slope = ((rise / 1000) / run) * 100
    return slope


def pipe_slope():
    print("==============================")
    print("       Slope Determiner       ")
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
                rise = float(input("What is the rise (mm)? "))
                run = float(input("What is the run (m)? "))

                if rise <= 0 or run <= 0:
                    print("Invalid input")
                    continue

            except ValueError:
                print("Invalid input")
                continue

            print(f"{round(calculate_slope(rise, run), 2)}%")
            break
