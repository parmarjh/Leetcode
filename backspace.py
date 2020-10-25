def check(S):
    string1 = '' 
    stack = []
    for i in range(len(S)-1,-1,-1):
        if S[i] == '#':
            stack.append('#')
            continue
        if stack:
            stack.pop()
            i-=1
            while(stack and S[i] != '#'):
                i-=1
                stack.pop()
            if S[i] == '#':
                stack.append('#')
            continue
        string1 += S[i]
    return string1


S,T = "bxj##tw","bxj###tw"

string1,string2 = check(S),check(T)

print(string1,"and",string2)
if string1 == string2:
    print(True)
else:
    print(False)
