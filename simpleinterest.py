def simpleinterest(p,t,r):
    St=(p*t*r)/100
    return St
P=int(input("Enter the Principle Amount (P):"))
T=int(input("Enter the Time(T):"))
R=int(input("Enter the rate(R):"))
print("The simple interest is",simpleinterest(P,T,R))

