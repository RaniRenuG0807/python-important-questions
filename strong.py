# Strong Number Practice
n=int(input("Enter Length of list "))
lis=[]
for i in range(n):
    element=int(input("Enter element of list "))
    lis.append(element)
print(lis)

lis2=[]
for num in lis:

    org_num=num
    sum=0
    while(num!=0):
        rem=num%10
        fact=1
        for i in range(1,rem+1):
            fact=fact*i
        sum=sum+fact
        num=num//10

    if(sum==org_num):
        print("Strong Number",sum)
        lis2.append(org_num)
    else:
        print("Not Strong",org_num)
print("Strong Numbers ",lis2)

