def userI(prompt, min_value, max_value):
    while True:
        try:
            number = int(input(prompt))
            if min_value <= number <= max_value:
                return number
            else:
                print("Input must be between", min_value, "and", max_value, "Try Again.")
        except ValueError:
            print("Invalid input. Please try again.")

def userII(prompt, min_value):
    while True:
        try:
            number = int(input(prompt))
            if number > min_value:
                return number
            else:
                print("Input must be greater than", min_value, "Try Again.")
        except ValueError:
            print("Invalid input. Please try again.")

def userIII(prompt, min_value):
    while True:
        try:
            number = int(input(prompt))
            if number >= min_value:
                return number
            else:
                print("Input must be greater than or equal to", min_value, "Try Again.")
        except ValueError:
            print("Invalid input. Please try again.")
