# PDF Form Filling Application

This application is designed to fill PDF forms using user input. It consists of two main Python scripts: `main.py` and `input.py`.

## main.py

The `main.py` script is responsible for reading the form fields from the PDFs, creating dictionaries with dynamically generated variable names and values, replacing certain values with user input, and writing the filled PDF.

It uses the `fillpdfs` module to get form fields from the PDF and to write the filled PDF. The form fields are stored in dictionaries, `data_dict` and `data_dict2`, which are then modified based on user input.

The script also defines pairs of values to be replaced and their replacements. It finds the keys that have the first two values as their values and replaces these values with the last value in the tuple.

The input values are obtained from the `get_input_values()` function imported from `input.py`. These values are assigned to the correct keys in `data_dict` and `data_dict2`.

The table values are obtained from the `get_table_values()` function also imported from `input.py`. These values are assigned to the correct keys in `data_dict` and `data_dict2`.

Finally, the script writes the filled PDF with the modified data and prints the form fields of the original PDFs.

## input.py

The `input.py` script contains two functions: `get_input_values()` and `get_table_values()`.

The `get_input_values()` function prompts the user to enter various details such as the vendor name, cost center, program number, total amount, purpose of the purchase, supervisor's phone number, location of the event, etc. These values are returned in a dictionary.

The `get_table_values()` function prompts the user to enter the values for 'd1', 'd2', 'd3', etc. in the format '1, bobas, $52'. If the user types "STOP", the remaining 'd' values are filled with white spaces. The entered values are returned in a dictionary.
