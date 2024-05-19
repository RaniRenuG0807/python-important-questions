# plandrome number using recursion
def plandrome(n):
    s=""
    if n==0:
        return s
    else:
        rem = n%10
        return str(rem) + plandrome(n//10)

num = int(input("Enter Number: "))
num_org = str(num)    
rev_num = plandrome(num)
print("Reverse Number: ",rev_num)
if(num_org==rev_num):
    print("Plandrome")
else:
    print("Not Plandrome")