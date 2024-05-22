# It worked. the best draft you will every see in your entire freaking life
#main.py
from fillpdf import fillpdfs
from input import get_input_values  # Import the function from your new file
from input import get_table_values  #from input import get_table_values

# Get form fields from the PDF
fields1 = fillpdfs.get_form_fields('FRF_DOC.pdf')
fields2 = fillpdfs.get_form_fields('BMF_DOC.pdf')

# Create a dictionary with dynamically generated variable names and values 'v1', 'v2', ...
data_dict = {key: f"d{i-16}" if 17 <= i <= 37 else f"f{i}" for i, (key, _) in enumerate(fields1.items(), start=0)}
data_dict2 = {key: f"b{i}" for i, (key, _) in enumerate(fields2.items(), start=0)}

# Create a new dictionary dict3 to store the value of 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7'
data_dict3 = {}

# Define the pairs of values to be replaced and their replacements
replacements = [('f9', 'b0', 'c1'), ('f5', 'f15', 'b4', 'c2'), ('f6', 'f16', 'b5', 'c3'), ('f38', 'b6', 'c4'), ('f7', 'b3', 'c5'), ('f4', 'b8', 'c6'), ('f1', 'b1', 'c7')]

for rep in replacements:
    # Find the keys that have the first two values as their values
    keys1 = [key for key, value in data_dict.items() if value in rep[:-1]]
    keys2 = [key for key, value in data_dict2.items() if value in rep[:-1]]
    
    # Replace these values with the last value in the tuple
    for key in keys1:
        data_dict[key] = rep[-1]
    for key in keys2:
        data_dict2[key] = rep[-1]
    
    # Store the replacement value in dict3 with the keys as the original values
    for key in keys1 + keys2:
        data_dict3[key] = rep[-1]

# Get the input values from the function you imported
input_values = get_input_values()

# Assign the input values to the correct keys in data_dict and data_dict2
for key, value in data_dict.items():
    if value in input_values:
        data_dict[key] = input_values[value]

for key, value in data_dict2.items():
    if value in input_values:
        data_dict2[key] = input_values[value]

# Get the table values from the function
table_values = get_table_values()

# Assign the table values to the correct keys in data_dict and data_dict2
for key, value in data_dict.items():
    if value in table_values:
        data_dict[key] = table_values[value]

# Write the filled PDF with the modified data
fillpdfs.write_fillable_pdf('FRF_DOC.pdf', 'Hope2.pdf', data_dict, flatten=False)
fillpdfs.write_fillable_pdf('BMF_DOC.pdf', 'Hope3.pdf', data_dict2, flatten=False)

# Print the form fields of the original PDFs
fillpdfs.print_form_fields('FRF_DOC.pdf')
fillpdfs.print_form_fields('BMF_DOC.pdf')
