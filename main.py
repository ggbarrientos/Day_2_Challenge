name = input("What is your name? ")
sales = int(input("How many sales do you have? "))
commissions = float(round((sales * 0.13),2))
print(f"{name} made {sales} sales, and is entitled to {commissions} commissions.")