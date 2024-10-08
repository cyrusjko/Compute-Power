def computepower(x,y):
    result = 1
    while y>0:
       if y%2 == 0:
         x=x*x
         y>>=1
       else:
          result=result*x
          y=y-1
    return result
x=int(input("Enter x for x^y: "))
y=int(input("Input y for x^y: "))
print(x,"to the power of ",y," is ",computepower(x,y))