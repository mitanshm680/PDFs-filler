#input.py
def get_input_values():
    return {
        'c1': input("Enter the vendor name: "),
        'c2': input("Enter the cost center: "),
        'c3': input("Enter the program number: "),
        'c4': input("Enter the total amount: "),
        'c5': input("Enter the purpose of the purchase: "),
        'c6': input("Enter the supervisor's phone number: "),
        'c7': input("Enter the location of the event: "),
        'f0': input("Enter the page no: "),
        'f2': input("Enter the Date of Purchase: "),
        'f3': input("Enter Your full name: "),
        'f10': input("Enter the telephone number of the vendor: "),
        'f11': input("Enter the address of the vendor(Don't write city/state/zip): "),
        'f12': input("Enter city/state/zip: "),
        'f14': input("Enter the last four digits of the Pcard: "),
        'b2': input("Enter the date of Event: "),
        'b7': input("Enter the name of your supervisor: "),
    }

def get_table_values():
    # Initialize an empty dictionary to store the input values
    input_values = {}

    # Flag to indicate when to stop the for loop
    stop = False

    # Loop over the range of dvalues
    for i in range(1, 22, 3):
        while True:
            # Get the input in the format you specified
            input_str = input(f"Enter the values for 'd{i}', 'd{i+1}', 'd{i+2}' in the format '1, bobas, $52': ")
            
            # Check if the user typed "STOP"
            if input_str.upper() == "STOP":
                # Fill the remaining 'd' values with white spaces
                for j in range(i, 22, 3):
                    input_values[f"d{j}"] = " "
                    input_values[f"d{j+1}"] = " "
                    input_values[f"d{j+2}"] = " "
                stop = True
                break
            
            # Split the input string by the comma and strip any leading/trailing whitespace
            input_list = [x.strip() for x in input_str.split(',')]
            
            # Check if the input list has the correct length
            if len(input_list) != 3:
                print(f"Invalid input for 'd{i}', 'd{i+1}', 'd{i+2}', please enter exactly 3 values separated by commas")
                continue
            
            # Store the input list in the dictionary
            input_values[f"d{i}"] = input_list[0]
            input_values[f"d{i+1}"] = input_list[1]
            input_values[f"d{i+2}"] = input_list[2]
            break

        # If stop is True, break the for loop
        if stop:
            break

    return input_values
