rent_amount = int(input("Enter the total cost of rent :R"))
food_cost = int(input("Enter the total cost of food :R"))
water_and_lights = int(input("Enter the total cost of water and lights :R"))
elec_charges = int(input("Enter the total cost of electricity charges :R"))
transport = int(input("Enter the total cost of transport :R"))

total_Amount = (rent_amount + food_cost + water_and_lights + elec_charges + transport)

print(f"Total Expense for the month are R{total_Amount}")
