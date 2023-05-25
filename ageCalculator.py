
age = input("How old are you?\n")
age = int(age)
#decades = age/10 # Integer division ## for whole number and integer division use "//"

decades = age // 10 # division
years = age % 10 # modulas sign -> reminder

print("decades : ", decades )

print("years", years)

print("Your are " + str(decades) + " Decades and " + str(years), "old.")

'''

Result:
/usr/bin/python3 /Users/flewbirds/Documents/FlewBirds/code-python/ageCalculator.py 
How old are you?
37
decades :  3
years 7
Your are 3 Decades and 7 old.

'''

