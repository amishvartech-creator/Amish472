# product name to product case converter

def convert_product_name(product_name, case_type):
    if case_type == "upper":
        return product_name.upper()
    elif case_type == "lower":
        return product_name.lower()
    elif case_type == "title":
        return product_name.title()
print("redmi note 12 pro".title())
print("redmi note 12 pro".upper())
print("redmi note 12 pro".lower())


        