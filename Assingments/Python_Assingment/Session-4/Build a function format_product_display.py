def format_product_display(name, price):
    """
    Takes a product name and price and returns a formatted display string.
    """
    return f"{name} - ₹{price}"

# Example usage:


product_name = 'Boat Earbuds'
product_price = 1299

formatted_output = format_product_display(product_name, product_price)
print(formatted_output)
