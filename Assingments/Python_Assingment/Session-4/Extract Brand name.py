# Extract Brand Name from Product String

product_string = "Apple iPhone 14 Pro Max"

# Find the index of the first space

first_space_index = product_string.find(" ")

# Extract the brand name (substring from start to first space)

brand_name = product_string[:first_space_index]

print("Extracted Brand Name:", brand_name)

