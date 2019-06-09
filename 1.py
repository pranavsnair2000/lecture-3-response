"""1. Write a Python program which accepts a sequence of comma-separated numbers from the user
 and generate a list and a tuple with those numbers. """

string=(input("Enter number string, seperated by commas :"))
s=string.split(",")
for i in s:
    i=int(i)
L=list(s)
T=tuple(s)
print("List  :",L)
print("Tuple  :",T)
