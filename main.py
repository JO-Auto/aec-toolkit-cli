from calculators import unit_converter
from calculators import pipe_slope

print("=============================")
print("  Engineering Utilities CLI")
print("=============================")

done = False
while not done:
    device = int(input(
        "Choose your calculator:\n"
        "1. Unit Converter\n"
        "2. Pipe Slope Calculator\n"
        "3. Exit\n"
    ))

    if device == 1:
        unit_converter.unit_converter()
    elif device == 2:
        pipe_slope.calculate_slope()
    else:
        done = True
