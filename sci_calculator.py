import sys  # import system module for use in sys_exit function
import math  # import math module for use in logarithm function


def sys_exit():  # function for closing program
    """ends program using sys module"""
    print('Thanks for using this calculator. Goodbye!')
    sys.exit()


def addition(val1, val2) -> float:  # function for adding 2 floating point numbers
    """adds val1 to val2"""
    output = val1 + val2
    return output


def subtraction(val1, val2) -> float:  # function for subtracting 2 floating point numbers
    """subtracts val2 from val1"""
    output = val1 - val2
    return output


def multiplication(val1, val2) -> float:  # function for multiplying 2 floating point numbers
    """multiplies val1 with val2"""
    output = val1 * val2
    return output


def division(val1, val2) -> float:  # function for dividing 2 floating point numbers
    """divides val1 by val2"""
    output = val1 / val2
    return output


def exponentiation(val1, val2) -> float:  # function for raising a floating point number to the power of another
    """val1 to the power of val2"""
    output = val1 ** val2
    return output


def logarithm(val1, val2) -> float:  # function for finding the log of a floating point number with a specific base
    """log base val1, val2"""
    output = math.log(val2, val1)
    return output


def main():  # main function that calls above functions as specified by the user
    """scientific calculator that can store previous
    outputs for future calculations"""

    running_total = 0  # defining variables for later use
    numb_of_runs = 0
    result = float(0)

    while True:  # main while loop displaying calculator menu
        print(f'Current Result: {result}\n')
        print('Calculator Menu\n---------------\n0. Exit Program\n1. Addition\n'
              '2. Subtraction\n3. Multiplication\n4. Division\n5. Exponentiation\n'
              '6. Logarithm\n7. Display Average\n')

        while True:  # secondary while loop necessary for jumping straight to menu selection

            try:  # error handling for when a user chooses a menu item not on the menu
                user_input = int(input('Enter Menu Selection: '))
                if user_input < 0 or user_input > 7:  # specifies allowable range of menu items for user to select
                    print('Error: Invalid selection!\n')
                    continue  # returns to secondary while loop (menu selection)

            except ValueError:
                print('Error: Invalid selection!\n')
                continue  # returns to secondary while loop (menu selection)

            if user_input == 7:  # calls previously defined variables at top of function
                try:  # error handling for if number of runs is 0 (cannot divide by 0 error); provides more control flow
                    avg_of_totals = running_total / numb_of_runs
                    print(f'Sum of calculations: {running_total:.2f}')  # :2f truncates decimals to 2 decimal places
                    print(f'Number of calculations: {numb_of_runs}')
                    print(f'Average of calculations: {avg_of_totals:.2f}\n')
                    continue
                except ZeroDivisionError:
                    print('Error: No calculations yet to average!')
                    continue

            if user_input == 0:  # calls function to close program
                sys_exit()
                break

            try:
                val1 = float(input('Enter first operand: '))  # error handling allows users to type RESULT or any other
            except ValueError:  # string to set operands as previous output
                val1 = result

            try:
                val2 = float(input('Enter second operand: '))
            except ValueError:
                val2 = result

            if user_input == 1:  # calls add function
                result = addition(val1, val2)
                running_total += result  # running total tracker
                numb_of_runs += 1  # number of runs counter
                break  # all following break statements brings code back to primary while loop (prints menu)

            elif user_input == 2:  # calls subtraction function
                result = subtraction(val1, val2)
                running_total += result
                numb_of_runs += 1
                break

            elif user_input == 3:  # calls multiplication function
                result = multiplication(val1, val2)
                running_total += result
                numb_of_runs += 1
                break

            elif user_input == 4:  # calls division function
                result = division(val1, val2)
                running_total += result
                numb_of_runs += 1
                break

            elif user_input == 5:  # calls exponent function
                result = exponentiation(val1, val2)
                running_total += result
                numb_of_runs += 1
                break

            elif user_input == 6:  # calls log function
                result = logarithm(val1, val2)
                running_total += result
                numb_of_runs += 1
                break


if __name__ == '__main__':  # runs main function (scientific calculator)
    main()
