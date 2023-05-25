'''

There are 6 Python Comparators

    '<' less than, '<=' less than equal to, '==' equal, '>=' greater than equal to, '>' greater than, '!=' not equal

if statement

An if statement lets us decide what to do: if TRUE, then do this

keyword 'or' combines multiple comparisions


'''

temperature = 75

if temperature > 80:
    print("It's too hot!")
    print("Stay inside")
elif temperature < 60:
    print("It's too cold!")
    print("Stay inside")
else:
    print("Enjoy the outdoors!")

##############

print("Short the code")

temperature = 75

if temperature > 80:
    print("Stay inside")
elif temperature < 60:
    print("Stay inside")
else:
    print("Enjoy the outdoors!")

#############
print("Smart code")

temperature = 75
# keyword 'or' combines multiple comparisions
if temperature > 80 or temperature < 60:
    print("Stay inside")
else:
    print("Enjoy the outdoors!")

##################


print("Smart code")

temperature = 75
forecast = "rain"
# keyword 'or' combines multiple comparisions
if temperature < 80 and forecast != "rain":
    print("Go Outside!")
else:
    print("Stay Inside!")

################

##################


print("Smart code")

temperature = 75
forecast = "rain"
# keyword 'or' combines multiple comparisions
if temperature < 80 and forecast != "rain":
    print("Go Outside!")
else:
    print("Stay Inside!")
####################


##################


print("Smart code")

temperature = 75
forecast = "sunny"
# keyword 'or' combines multiple comparisions
if temperature < 80 and forecast != "rain":
    print("Go Outside!")
else:
    print("Stay Inside!")

######################

print("Smart code")

forecast = "rain"
# keyword 'not' lets you negate a comparision.
if not forecast == "rain":
    print("Go Outside!")
else:
    print("Stay Inside!")

#######################

raining = True

if raining:
    print("Go Inside")
else:
    print("Stay Inside!")

###################

raining = True

if not raining:
    print("Go outside!")
else:
    print("Stay Inside")

###################


