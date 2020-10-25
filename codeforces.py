#link :https://codeforces.com/contest/1397/problem/A

n = int(input())

while(n):
    n-=1
    lenght = int(input())
    lenght_copy = lenght
    arr = [0]*26
    while(lenght):
        lenght -= 1
        string = input()
        for i in string:
            arr[ord(i) - ord('a')] += 1
    # print(arr)
    flag =0
    for i in arr:
        if i == 0:
            continue
        if i%lenght_copy != 0:
            print("No")
            flag = 1
            break
    if not flag:
        print("YES")
    
