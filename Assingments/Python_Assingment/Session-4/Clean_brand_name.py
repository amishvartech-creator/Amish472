# function to clean brand name

def clean_brand_name(brand_name):
    # remove leading and trailing whitespace
    brand_name = brand_name.strip()

    # convert to title case

    brand_name = brand_name.title()
    return brand_name

print(clean_brand_name("  samsung-galaxy  "))
print(clean_brand_name("  oneplus-nord  "))

# Extract brand name and model using split() and slicing
print("\n--- Extracting Brand Name and Model ---")
product_string = 'Apple iPhone 14 Pro Max'

# Split the string by space to find where brand ends
words = product_string.split()
print(f"Words: {words}")

# The brand name is the first word
# We can use slicing with the index of the first space
first_space_index = product_string.find(' ')
brand_name = product_string[:first_space_index]  # Slice from start to first space
model_name = product_string[first_space_index + 1:]  # Slice from after first space to end

print(f"\nOriginal String: '{product_string}'")
print(f"Brand Name: '{brand_name}'")
print(f"Model: '{model_name}'")

# Extract brand name and model using split() and slicing
print("\n--- Extracting Brand Name and Model ---")
product_string = 'Apple iPhone 14 Pro Max'

# Split the string by space to find where brand ends
words = product_string.split()
print(f"Words: {words}")

# The brand name is the first word
# We can use slicing with the index of the first space
first_space_index = product_string.find(' ')
brand_name = product_string[:first_space_index]  # Slice from start to first space
model_name = product_string[first_space_index + 1:]  # Slice from after first space to end

print(f"\nOriginal String: '{product_string}'")
print(f"Brand Name: '{brand_name}'")
print(f"Model: '{model_name}'")
