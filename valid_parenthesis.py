

# link : https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3301/

# Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
# An empty string is also valid.

s = "(*)(*((**"
s = "(()*()"
stack = 0
stars = 0
s = list(s)
for i in s:
    print(i)
    if i == '(':
        for j in s:
            if  j == ')':
                s.remove(j)
                break
        else:
            for j in s:
                if j == '*':
                    s.remove(j)
                    break
            else:
                print("False, not found")
            
    elif i == '*':
        stars +=1
        continue

    elif i == ')':
        if not stars:
            print("not founde star before for ) ")
            break
        stars-=1
else:
    print("Succeesss")


