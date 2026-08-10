from calculators import unit_converter
from calculators import pipe_slope

print("=============================")
print("  Engineering Utilities CLI")
print("=============================")

running = True
while running:
    try:
        device = int(input(
            "Choose your calculator:\n"
            "1. Unit Converter\n"
            "2. Pipe Slope Calculator\n"
            "3. Exit\n"
        ))

    except ValueError:
        print("Invalid input")

    else:
        if device == 1:
            unit_converter.unit_converter()
        elif device == 2:
            pipe_slope.calculate_slope()
        elif device == 3:
            running = False
        else:
            print("Invalid input")
