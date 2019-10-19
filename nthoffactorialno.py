def fib(n):
    if n<=0:
        print("Wrong input")
    elif (n==1):
        return 0
    elif(n==2 or n==3):
        return 1
    else:
        return (fib(n-1)+fib(n-2))
f=int(input("Enter the nth of fibonacci number:"))
print(fib(f))