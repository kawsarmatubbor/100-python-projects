print("Welcome to Temperature Converter")
while True:
    print("1. Celsius to Fahrenheit")
    print("2. Celsius to Kelvin")
    print("3. Fahrenheit to Celsius")
    print("4. Fahrenheit to Kelvin")
    print("5. Kelvin to Celsius")
    print("6. Kelvin to Fahrenheit")
    print("0. Exit")

    option = input("Choose an option: ")

    if option == "0":
        break
    else:
        temperature = float(input("Enter temperature: "))
        if option == "1":
            print(f"{(temperature * 1.8) + 32} Fahrenheit\n")
        elif option == "2":
            print(f"{temperature + 273.15} Kelvin\n")
        elif option == "3":
            print(f"{(temperature - 32) * 1.8} Celsius\n")
        elif option == "4":
            print(f"{((temperature - 32) * 1.8) + 273.15} Kelvin\n")
        elif option == "5":
            print(f"{temperature - 273.15} Celsius\n")
        elif option == "6":
            print(f"{(temperature - 273.15) * 1.8 + 32} Fahrenheit\n")
        else:
            print("Invalid option. Try again.")