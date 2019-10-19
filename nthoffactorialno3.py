#dynamicprogrammingsolution
FibArray=[0,1]
def fib(n):
    if (n<=0):
        print("Wrong Input")
    elif(n<=len(FibArray)):
        return FibArray[n-1]
    else:
        temp_fib=(fib(n-1)+fib(n-2))
        FibArray.append(temp_fib)
        return temp_fib
print(fib(9))  