'''

Sales tax Calculator

'''

amount = 10
tax = .06

total = amount + amount*tax

print(amount, tax, total)

#################

amount_int = int(10.6)

tax_int = .07

total = amount_int + amount_int*tax_int

#total = str(total)

print("amount_int:", amount_int, "tax_int", tax_int, "Total Amount", str(total))


#name = "Rama Krishna"
name = input("What is your name: \n")

customer_greetings = "Welcome mr. " + name

print(customer_greetings)
