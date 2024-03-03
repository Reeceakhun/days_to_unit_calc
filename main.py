calculate_to_seconds = 24 * 60 * 60

name_of_unit = "seconds"

#def days_to_unit():
 #   print (f"{days} days are {days * calculate_to_seconds} {name_of_unit}")

#days_to_unit()

def days_to_unit(days):
    if days > 0:
        return (f"{days} days are {days * calculate_to_seconds} {name_of_unit}")
    elif days == 0:
        return "You entered zero, please enter a valid positive number"

    else:
        return "You entered a wrong value"

def validate_and_execute ():
    if user_input.isdigit():
        user_input_number = int(user_input)
        if user_input_number > 0:
            calculated_value = days_to_unit(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print ("You entered zero, please enter a valid positive number")
    else:
        print("You entered a non-digit value, don't ruin my program")


user_input = input("Please enter the number of days\n")
# convert the user input from string to integer
validate_and_execute()


user_input = input("Please enter the number of days\n")
# convert the user input from string to integer
validate_and_execute()