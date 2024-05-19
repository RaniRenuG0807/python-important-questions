# Print N natural numbers using recursion
def rec(num,start=0):
    if(start==num):
        return start
    else:
        print(start)
        return rec(num,start+1) 

num=int(input("Enter Num From "))
num_till=int(input("Enter Num Till "))      
result = rec(num_till,num)
print(result)
