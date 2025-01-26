from fibonacci import Fibonacci


def display_menu():
    print("\n" + "=" * 40)
    print("    Welcome to Fibonacci Sequence Generator")
    print("=" * 40)

    created = False
    myFibonacci = None

    while True:
        print("\nPlease choose an option:")
        print("1. Create Fibonacci sequence. Default number of iterations 0.")
        print("2. Get number of iterations.")
        print("3. Get sequence.")
        print("4. Set number of iterations.")
        print("5. Set sequence.")
        print("0. Exit.")

        try:
            option = int(input("\nEnter your choice: "))
        except ValueError:
            print("Invalid input, please enter a number between 0 and 5.")
            continue

        if option == 1:
            if created:
                print("\nFibonacci sequence already created!")
            else:
                print("\nCreating Fibonacci sequence with default iterations...")
                myFibonacci = Fibonacci()
                created = True

        elif option == 2:
            if created:
                print(f"\nNumber of iterations: {myFibonacci.get_iterations()}")
            else:
                print("\nNo Fibonacci sequence created yet.")

        elif option == 3:
            if created:
                print(f"\nFibonacci sequence: {myFibonacci.get_sequence()}")
            else:
                print("\nNo Fibonacci sequence created yet.")

        elif option == 4:
            if created:
                try:
                    new_iterations = int(input("\nEnter new number of iterations: "))
                    myFibonacci.set_iterations(new_iterations)
                    print(f"Number of iterations updated to {new_iterations}.")
                except ValueError:
                    print("Invalid input. Please enter an integer.")
            else:
                print("\nNo Fibonacci sequence created yet.")

        elif option == 5:
            if created:
                myFibonacci.set_sequence()
                print("\nFibonacci sequence has been updated.")
            else:
                print("\nNo Fibonacci sequence created yet.")

        elif option == 0:
            print("\nThank you for using the Fibonacci Generator. Goodbye!")
            break

        else:
            print("\nInvalid option, please choose a valid number between 0 and 5.")

        print("\n" + "-" * 40)
