# Function to check if discount is applicable

def is_discount_applicable(order_amount):
    
    if order_amount > 500:
        return True
    else:
        return False
print("Discount applicable:", is_discount_applicable(750))  
print("Discount applicable:", is_discount_applicable(450))  

is_discount_applicable(750)  
is_discount_applicable(450)  
