name="John doe"
age=20
course="python programming"
college="abc university"
email="john@example.com"
print("╔" + "═" * 32 + "╗")
print("║{:^32}║".format("STUDENT BIO CARD"))
print("╠" + "═" * 32 + "╣")
print(f"║Name:{name:<20}║")
print(f"║Age:{age}years{' '*(20-len(str(age)+'years'))}║")
print(f"║Course:{course:<20}║")
print(f"║College:{college:<20}║")
print(f"║Email :{email:<20}║")
print("╚"+"═"*32+"╝")