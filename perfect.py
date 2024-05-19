# perfect number using recursion
def perfect(num,incre):
    sum=0
    if(incre==num):
        return sum
    elif(num%incre==0):
        sum=sum+incre
    return perfect(num,incre+1)+sum

num=int(input("Enter Number: "))
result=perfect(num,incre=1)
print("sum of factors",result)
if(result==num):
    print("Perfect Number")
else:
    print("Not Perfect")

# Using loop
num=int(input("Enter Number "))
incre=1
sum=0
while(incre<num):
    if(num%incre==0):
        sum=sum+incre
    incre+=1
if(sum==num):
    print("Perfect")
else:
    print("Not Perfect")