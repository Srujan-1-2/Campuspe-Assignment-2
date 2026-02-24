age = int(input("Enter age: "))
day = input("Enter day of week: ")
tickets = int(input("Enter number of tickets: "))
if age < 3:
    price = 0
    category = "Free"
elif age <= 12:
    price = 150
    category = "Child"
elif age <= 59:
    price = 300
    category = "Adult"
else:
    price = 200
    category = "Senior"
base_price = price * tickets
day = day.lower()
if day in ["friday", "saturday", "sunday"]:
    discount = base_price * 0.20   
else:
    discount = 0
final_price = base_price - discount
print("\nTicket Category:", category)
print("Base Price: ₹", base_price)
print("Discount: ₹", discount)
print("Price After Discount: ₹", final_price)
print("Total Amount to Pay: ₹", final_price)