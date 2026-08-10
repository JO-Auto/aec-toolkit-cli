from calculators import unit_converter
from calculators import pipe_slope
from calculators import material_estimator
from calculators import water_tank_sizing
from calculators import pipe_flow

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
            "4. Water Tank Sizing\n"
            "5. Pipe Flow / Pipe Sizing Calculator\n"
            "6. Exit\n"
        ))

    except ValueError:
        print("Invalid input")
        continue

    if device == 1:
        unit_converter.unit_converter()
    elif device == 2:
        pipe_slope.pipe_slope()
    elif device == 3:
        material_estimator.material_estimator()
    elif device == 4:
        water_tank_sizing.water_tank_sizing()
    elif device == 5:
        pipe_flow.pipe_flow()
    elif device == 6:
        running = False
    else:
        print("Invalid input")
