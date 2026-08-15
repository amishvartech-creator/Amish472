# Zomato Order Bill Calculator

# Take user input as string
order_price_string = input("Enter Zomato order price: ")

# Convert string to float using type casting
order_price = int(order_price_string)

# Calculate 18% GST
gst = order_price * 0.18

# Calculate final bill
final_bill = order_price + gst

# Print the results
print("Order Price: " + str(order_price))
print("GST (18%): " + str(gst))
print("Final Bill Amount: " + str(final_bill))
