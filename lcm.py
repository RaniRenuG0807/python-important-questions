# LCM using Recursion
def lcm(greater,num1,num2):
    if(greater%num1==0 and greater%num2==0):
        return greater
    else:
        return lcm(greater+1,num1,num2)

num1=int(input("First Number: "))
num2=int(input("Second Number: "))
if(num1>num2):
    greater = num1
else:
    greater = num2
result=lcm(greater,num1,num2)
print(f"lcm{num1} and {num2} is {result}")


# LCM of 3 numbers using loop
num1 = int(input("Enter First "))
num2 = int(input("Enter Second "))
num3 = int(input("Enter Third "))
if(num1>num2 and num1>num3):
    max = num1
elif(num2>num1 and num2>num3):
    max=num2
else:
    max=num3
while(True):
    if(max%num1==0 and max%num2==0 and max%num3==0):
        break
    max+=1
print(f"lcm is {max}")