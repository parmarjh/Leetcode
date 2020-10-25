
# n = int(input())
# while(n):
#     n-=1
#     N, X = map(int, input().split())
#     arr = len(set(map(int, input().split())))
#     if (arr > X):
#         print('Average')
#     if (arr == X):
#         print('Good')
#     if (arr < X):
#         print('Bad')


# s =input()
# ss = list(set(s))
# ans = ""
# for i in s:
#     if i in ss:
#         ans += i
#         ss.remove(i)
# print(ans)
def main():
    n = int(input())
    s = []
    while(n):
        n-=1
        s.append(int(input()))
    aa =s.count(1)
    print(str(aa))
    return 
main()
