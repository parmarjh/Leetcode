lst1 = [1,2,3,5,6,7]
lst2 = []
i = 0
j = 0
ans = []
while not(i > len(lst1)-1 and j > len(lst2)-1):
    if lst1[i] < lst2[j]:
        ans.append(lst1[i])
        i+=1
    elif lst1[i] > lst2[j]:
        ans.append(lst2[j])
        j+=1
    else:
        ans.append(lst1[i])
        ans.append(lst2[j])
        i+=1
        j+=1
    if i == len(lst1):
        ans.extend(lst2[j:])
        break
    if j == len(lst2):
        ans.extend(lst1[i:])
        break

print(ans)

