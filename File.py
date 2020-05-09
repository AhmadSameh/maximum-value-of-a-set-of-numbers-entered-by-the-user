N=int(input("Enter how many numbers to calculate: "))
i=0
for i in range(i,N,1):
    x=int(input("Enter Number: "))
    if i==0:
        max=x
        min=x
    if x>max:
        max=x
    elif x<min:
        min=x
print("Maximum value is: ", max)
print("Minimum value is: ", min)