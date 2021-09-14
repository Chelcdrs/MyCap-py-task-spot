a=0
b=1
c=a+b
n=int(input("Enter the last term to print Fibonacci numbers(not less than 3): "))
print("The first ",n," Fibonacci numbers are: ",a,", ",b,", ",c,end=" ")
if n>2:
    for i in range(3,n):
        a=b
        b=c
        c=a+b
        print(", ",c,end="")