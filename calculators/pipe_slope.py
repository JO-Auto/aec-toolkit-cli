def determine_slope():
    print("=============================")
    print("      Determining Slope      ")
    print("=============================")

    rise = float(input("What is the rise you want to determine the slope? "))
    run = float(input("And the run? "))

    slope = (rise / run) * 100
    print(f"{slope} %")
