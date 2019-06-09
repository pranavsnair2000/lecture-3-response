#4. Write a Python program to calculate the sum of the digits in an integer.
def dig_sum(x):
    if x==0:
        return 0
    else:
        return x%10 + dig_sum(x//10)
a=input("enter number to check sum of digits \n")
if(a.isnumeric()):
    a=int(a)
    print(dig_sum(a))
else:
    print("not an integer")
