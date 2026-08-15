# The original list of messy product names
messy_names = [' mi-Band 5 ', ' SAMSUNG-Galaxy ', ' realme-Book ']

# Cleaning the list using a list comprehension and string methods
cleaned_names = [name.strip().replace('-', ' ').title() for name in messy_names]

# Printing the final cleaned list
print(cleaned_names)