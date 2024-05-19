# Armstrong Number Using Recursion
def armstrong(num,pow):
    sum = 0
    if (num==0):
        return sum
    else:
        rem = num%10
        arm = rem**pow
        sum = sum + arm
        return sum + armstrong(num//10,pow)

number = int(input("Enter Number: "))
num_s = str(number)
power = len(num_s)
result = armstrong(number,power)
if(result==number):
    print(f"{number} is Armstrong Number")
else:
    print(f"{number} Not Armstrong Number")
