#***find the value of factorial of a number***
n=int(input("enter a number"))
sum=1
for x in range(1,n+1,1):
    sum=sum*x
print('the factorial of a number:',sum)
