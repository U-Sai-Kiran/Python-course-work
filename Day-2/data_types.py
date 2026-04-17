#Data Types
#1. Numeric Types
product_quantity = 3
order_id = 10987432
print(order_id)

#b. float – Floating-point
product_price = 749.99
discount_percentage = 15.5
average_rating = 4.3
print(average_rating)

#c. complex – Complex Numbers
z = 5 + 2j # Not commonly used in typical e-commerce workflows

#2. Sequence Types
customer_name = "Rohit Sharma"
delivery_address = "Bangalore, Karnataka"
product_category = "Electronics"
print(customer_name)

#b. list – List
cart_items = ["Shoes", "T-shirt", "Headphones"]
top_categories = ["Mobiles", "Fashion", "Home", "Beauty"]
print(cart_items)

#c. tuple – Tuple
warehouse_location = (12.9716, 77.5946) # Latitude and Longitude
product_dimensions = (12.5, 9.8, 2.2) # Length, Width,
Height in inches

#3. Set Types
available_sizes = {"S", "M", "L", "XL"}
popular_brands = {"Nike", "Adidas", "Puma", "Nike"} # 'Nike' only once
print(popular_brands)

#b. frozenset – Immutable Set
frozen_tags = frozenset(["Sale", "Limited Edition", "Trending"])
print(frozen_tags)

#4. Mapping Type
product_details = {
"name": "Wireless Mouse",
"brand": "Logitech",
"price": 899.99,
"rating": 4.5
}
customer_profile = {
"name": "Anjali Verma",
"email": "anjali@example.com",
"prime_member": True
}
print(product_details,customer_profile)

#5. Boolean Type
is_logged_in = True
is_payment_successful = False
is_in_stock = True
print(is_in_stock)

#6. None Type
tracking_number = None
delivery_partner = None
print(tracking_number)

#Checking the Type in Python
print(type(product_price)) # <class 'float'>
print(type(cart_items)) # <class 'list'>
print(type(is_in_stock)) # <class 'bool'>
