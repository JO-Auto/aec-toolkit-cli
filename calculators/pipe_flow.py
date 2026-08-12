import math

STANDARD_PIPE_DIAMETERS = [15, 20, 25, 32, 40, 50, 65, 80, 100, 125, 150, 200, 250, 300]


def calculate_pipe_flow(diameter, velocity):
    area = (math.pi * (diameter / 1000) ** 2) / 4
    flow_rate = area * velocity
    flow_rate_liters = flow_rate * 1000

    return flow_rate, flow_rate_liters


def calculate_pipe_diameter(flow_rate, velocity):
    area = (flow_rate / 1000) / velocity
    diameter = math.sqrt((area * 4) / math.pi) * 1000

    return diameter


def find_standard_pipe_diameter(diameter):
    for standard_diameter in STANDARD_PIPE_DIAMETERS:
        if standard_diameter >= diameter:
            return standard_diameter

    return None


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
                    diameter = float(input("What is the diameter of the pipe (mm)?\n"))
                    velocity = float(input("What is the velocity of the water (m/s)?\n"))

                    if diameter <= 0 or velocity <= 0:
                        print("Invalid input")
                        continue

                    if velocity < 0.6:
                        print("Warning: the velocity is below the recommended range")
                    elif velocity > 2.5:
                        print("Warning: the velocity is above the recommended range")

                except ValueError:
                    print("Invalid input")
                    continue

                flow_rate, flow_rate_liters = calculate_pipe_flow(diameter, velocity)

                print(f"The flow rate is {round(flow_rate_liters, 2)} L/s ({round(flow_rate, 2)} m³/s)")
                break

        elif choice == 2:
            while True:
                try:
                    flow_rate = float(input("What is the flow rate of the water (L/s)?\n"))
                    velocity = float(input("What is the velocity of the water (m/s)?\n"))

                    if flow_rate <= 0 or velocity <= 0:
                        print("Invalid input")
                        continue

                    if flow_rate < 0.1:
                        print("Warning: flow rate is below the recommended range")
                    elif flow_rate > 100:
                        print("Warning: flow rate is above the recommended range")

                    if velocity < 0.6:
                        print("Warning: the velocity is below the recommended range")
                    elif velocity > 2.5:
                        print("Warning: the velocity is above the recommended range")

                except ValueError:
                    print("Invalid input")
                    continue

                required_diameter = (calculate_pipe_diameter(flow_rate, velocity))

                recommended_diameter = find_standard_pipe_diameter(required_diameter)

                if recommended_diameter is None:
                    print("The required diameter exceeds the currently supported sizes")
                    break

                print(
                    f"Calculated diameter: {round(required_diameter, 2)} mm\n"
                    f"Recommended standard diameter: {recommended_diameter} mm")
                break

        elif choice == 3:
            return
