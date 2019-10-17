def compoundinterest(p,t,r):
    CI=p*(pow((1+r/100),t))
    return CI
P=int(input("Enter the Principle Amount:"))
T=int(input("Enter the Time Span:"))
R=int(input("Enter the Rate:"))
print("The compound interest is",compoundinterest(P,T,R))