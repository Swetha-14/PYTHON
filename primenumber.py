start=int(input("Enter the starting value:"))
end=int(input("Enter the ending value:"))
for number in range(start,end+1):
    for x in range(2,number):
        if (number%x)==0:
            break
        else:
            print(number)