from itertools import combinations
value,k=map(int,input().split())
value_len=len(str(value))
list1=list(combinations(str(value),value_len-k))
list1.sort()
print(*list1[0],sep='')
