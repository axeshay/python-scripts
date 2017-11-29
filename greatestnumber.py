def greatest_number(a,b,c):
    if (a > b) and (a > c):
        largest = a
        return a
    elif (b > a) and (b > c ):
        largest = b
        return b
    else:
        largest = c
        return c
a = int(input("Enter first number\n"))
b = int(input("Enter second number\n"))
c = int(input("Enter third number\n"))
print("the greatest number is :\n")
print(greatest_number(a,b,c))
