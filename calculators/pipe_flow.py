import math


def calculate_pipe_flow(diameter, velocity):
    area = (math.pi * diameter ** 2) / 4
    flow_rate = area * velocity
    flow_rate_liters = flow_rate * 1000

    return flow_rate, flow_rate_liters


def pipe_flow():
    print("==================================")
    print("Pipe Flow / Pipe Sizing Calculator")
    print("==================================")

    while True:
        try:
            choice = int(input("1. Pipe Flow Calculator\n"
                               "2. Pipe Sizing Calculator\n"
                               "3. Back\n"))
            if not 1 <= choice <= 3:
                print("Invalid input")
                continue

        except ValueError:
            print("Invalid input")
            continue

        if choice == 1:
            while True:
                try:
                    diameter = float(input("What is the diameter of the pipe (m)?\n"))
                    velocity = float(input("What is the velocity of the water (m/s)?\n"))

                    if diameter <= 0 or velocity <= 0:
                        print("Invalid input")
                        continue

                except ValueError:
                    print("Invalid input")
                    continue

                flow_rate, flow_rate_liters = calculate_pipe_flow(diameter, velocity)

                print(f"The flow rate is {round(flow_rate_liters, 2)} L/s ({round(flow_rate, 2)} m³/s)")
                break

        elif choice == 2:
            print("Pipe Sizing Calculator - Coming Soon")

        elif choice == 3:
            return
