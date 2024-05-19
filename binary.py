# Decimal to Binary using Recursion Function
def binary(num):
    res = ""
    if(num==0):
        return res
    else:
        rem = num%2
        return binary(num//2) + str(rem)

num = int(input("Enter Number: "))
result = binary(num)
print(result)

# Using Loop
num = int(input("Enter Value "))
res = ""
while(num!=0):
    rem = num%2
    num = num//2
    res = str(rem) + res
print(res)
    