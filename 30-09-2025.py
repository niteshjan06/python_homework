"""
to convert a integer number into binary than change its 2nd lsb to 1 and then again convert it to integer value.
"""

# main code

number = int(input("Enter any number: "))
binary = bin(number)
binary_list = list(str(binary))
binary_list[-2] = '1'
str="".join(binary_list)

print(int(str,2))