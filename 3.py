"""3. Write a python program for binary search to search a number in the list of given numbers.
If the number isn't present, give the appropriate message.
Both the list and the number to be searched is given by the user."""

def binarySearch(ar,low,high,x):
    pos=-1
    mid=1+(low+high)//2
    if(high>low):
        if x==ar[mid]:
            pos= mid
        elif(x>ar[mid]):
            return binarySearch(ar,mid+1,high,x)
        elif(x<ar[mid]):
            return binarySearch(ar,low,mid-1,x)
    return pos
l=[]
n=int(input("Enter number of elements in array :  "))
for i in range(0,n):
    l.append(int(input()))
l.sort()
print("array : ",l)

x=int(input("Enter element to search for : "))

res=binarySearch(l,0,n,x)

if res==-1:
    print(x,"not in the list")
else:
    print("index of ",x,"is",res)
