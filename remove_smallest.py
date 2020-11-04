n = int(input())
while(n):
    n-=1
    length = int(input())
    data = list(map(int, input().split()))
    data.sort()
    flag = False
    for i in range (length-1):
        if data[i+1] - data[i] > 1 :
            print("NO")
            flag = True
            break
    if not flag:
        print("YES")



