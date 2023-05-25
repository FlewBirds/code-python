# import re
# import sys
#
#
# input_wtspace=str(input("Enter your sentence without spaces and with capital letter words\n"))
#
# if input_wtspace == "":
# #    print("Please enter text with out spaces or it should not be null")
#     sys.exit("Please enter text with out spaces or it should not be null")
# elif ' ' in input_wtspace:
# #    print("Please enter text with out spaces or it should not be null")
#     sys.exit("Please enter text with out spaces or it should not be null")
# else:
#     print("Processing your string to seperate the charecters")
#
# print("Split delimiter is Capital letter and give space before all capital letters")
#
# print("Initial String", input_wtspace)
#
# my_list = re.findall('[a-zA-Z][^A-Z]*', input_wtspace)
#
# print(my_list)
#
# def listToString(my_list):
#     str1 =" "
#     return (str1.join(my_list))
#
# print("Expected result is: ", listToString(my_list))
###########


import re
import sys


input_wtspace=str(input("Enter your sentence without spaces and with capital letter words\n"))

if input_wtspace == "":
#    print("Please enter text with out spaces or it should not be null")
    sys.exit("Please enter text with out spaces or it should not be null")
elif ' ' in input_wtspace:
#    print("Please enter text with out spaces or it should not be null")
    sys.exit("Please enter text with out spaces or it should not be null")
else:
    print("Processing your string to seperate the charecters")

print("Split delimiter is Capital letter and give space before all capital letters")

print("Initial String", input_wtspace)

my_list = re.findall('[a-zA-Z][^A-Z]*', input_wtspace)

print(" ".join(my_list))