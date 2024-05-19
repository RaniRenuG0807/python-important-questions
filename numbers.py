# First N natural number
'''num=int(input("Enter Number "))
n=0
while(n<=num):
    print(n)
    n+=1'''

# First N natural number using recursion
'''def natural_num(num,n=0):
    if(n==num):
        return n
    print(n)
    return natural_num(num,n+1)
num=5
print(natural_num(num))'''

# n natural numbers in reverse order
'''num=5
while(num>=0):
    print(num)
    num-=1'''

# N natural number(reversed) using Recursion
'''def reverse_natural(num):
    if(num==0):
        return num
    print(num)
    return reverse_natural(num-1)
num=7
result = reverse_natural(num)'''

# first N odd Natural Numbers
'''num = 10
n=1
while(n<=num):
    if(n%2!=0):
        print(n)
    n+=1'''

# First N odd numbers using recursion
'''def odd(num,n=1):
    if(n==num):
        return n
    elif(n%2!=0):
        print(n)
    return odd(num,n+1)
num=15
result = odd(num)
print(result)'''

# First N even Numbers
'''num=20
n=1
while(n<=num):
    if(n%2==0):
        print(n)
    n+=1'''

# First N even Numbers Using Recursion
'''def even(num,n=1):
    if(n==num):
        return n
    elif(n%2==0):
        print(n)
    return even(num,n+1)
num=16
result=even(num)
print(result)'''

# First N Odd Numbers in Reverse order
'''num=20
while(num>=0):
    if(num%2!=0):
        print(num)
    num-=1'''

# First N Odd Numbers in Reverse order using Recursion
'''def reverse_odd(num):
    if(num==1):
        return num
    elif(num%2!=0):
        print(num)
    return reverse_odd(num-1)
num=20
print(reverse_odd(num))'''

# First N even Numbers Reversed
'''num=24
while(num>=0):
    if(num%2==0):
        print(num)
    num-=1'''

# First N even Numbers Reversed using Recursion
'''def reverse_even(num):
    if(num==0):
        return num
    elif(num%2==0):
        print(num)
    return reverse_even(num-1)
num=18
print(reverse_even(num))'''
