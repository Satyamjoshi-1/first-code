a=int(input("enter number"))
b=0
while a>0:
    c=a%10
    b=b+c
    a=(a-c)/10
print("sum of digits in a is",b)    
