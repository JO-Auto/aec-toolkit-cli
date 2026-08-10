from calculators import unit_converter
from calculators import pipe_slope
from calculators import material_estimator

print("==============================")
print("   Engineering Utilities CLI   ")
print("==============================")

running = True
while running:
    try:
        device = int(input(
            "Choose your calculator:\n"
            "1. Unit Converter\n"
            "2. Pipe Slope Calculator\n"
            "3. Material Estimator\n"
            "4. Exit\n"
        ))

    except ValueError:
        print("Invalid input")
        continue

    if device == 1:
        unit_converter.unit_converter()
    elif device == 2:
        pipe_slope.calculate_slope()
    elif device == 3:
        material_estimator.material_estimator()
    elif device == 4:
        running = False
    else:
        print("Invalid input")
