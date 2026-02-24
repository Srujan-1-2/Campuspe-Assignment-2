total_bill_amount=int(input("Enter total bill:"))
no_of_people=int(input("Number of people:"))
tax_percentage=int(input("Enter tax percentage:"))
tip_percentage=int(input("Enter tip percentage:"))
print("Subtotal: ", total_bill_amount)
tax=(total_bill_amount*tax_percentage)/100
print("Tax (", tax_percentage, "%):", tax)
after_tax=total_bill_amount+tax
print("After tax:", after_tax)
tip=(after_tax*tip_percentage)/100
print("Tip (", tip_percentage, "%):", tip)
total=total_bill_amount+tax+tip
print("Total:", total)
split=total/no_of_people
print("Per person: ", split)