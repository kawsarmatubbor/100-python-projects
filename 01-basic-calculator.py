print("Welcome to Basic Calculator")
while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("0. Exit")

    option = input("Choose an option: ")

    if option == "0":
        print("Thank you for using Basic Calculator.")
        break
    else:   
        first_number = int(input("Enter your first number: "))
        second_number = int(input("Enter your second number: "))

        if option == "1":
            print(f"Your result is {first_number + second_number}\n")
        elif option == "2":
            print(f"Your result is {first_number - second_number}\n")
        elif option == "3":
            print(f"Your result is {first_number * second_number}\n")
        elif option == "4":
            print(f"Your result is {first_number / second_number}\n")
        else:
            print("Invalid option. Try again.")