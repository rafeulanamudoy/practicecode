from math import *
number1=float(input("enter first number"))
operator=input("enter operator")
number2=float(input("enter second number"))
if operator=="+":
    print("the result is:",number1+number2)
elif operator=="-":
    print("the result is:", number1 - number2)
elif operator=="/":
    print("the result is:", number1/number2)
elif operator=="*":
    print("the result is:", number1*number2)
elif operator=="%":
    print("the result is:", number1 % number2)
elif operator=="^":
    print("the result is:", pow(number1,number2))
elif operator=="√ ":
    print("the result is:",sqrt(number1,number2))
else:
    print("invalid operator")
