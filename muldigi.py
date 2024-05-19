# Multiply of all digits of given number using recursion
def digits(num,mul=1):
    if(num==0):
        return mul
    else:
        rem = num%10
        mul = mul*rem
        return digits(num//10,mul) 

number=int(input("Enter Number: "))
print(digits(number))