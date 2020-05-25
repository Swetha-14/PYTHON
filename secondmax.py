if __name__ == '__main__':
    n = int(input())
    if n > 2 and n <= 10:
        arr = list(map(int, input().split()))
        mylist = list( dict.fromkeys(arr) )
        mylist.sort()
        mylist.pop()
        print(mylist[-1])
            
