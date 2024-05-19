# HCF using Recursion
def hcf(max,min,res,n):
    if(n>min):
        return res
    elif(max%n==0 and min%n==0):
        res = n
    return hcf(max,min,res,n+1)

num1 = int(input("Enter value "))
num2 = int(input("Enter VAlue "))
if(num1>num2):
    max=num1
    min=num2
else:
    max=num2
    min=num1

result_hcf = hcf(max,min,res=1,n=1)
print(result_hcf)

# HCF using loop
num1 = int(input("Enter Number ")) 
num2 = int(input("Enter Number "))
if(num1>num2):
    max = num1
    min = num2
else:
    max = num2
    min = num1
n=1
while(n<=min):
    if(max%n==0 and min%n==0):
        print(n)
        res = n
    n+=1
print(f"HCF of {num1} and {num2} is {res}")