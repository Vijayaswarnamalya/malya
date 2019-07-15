'''s=['kk',2]
b=[]
b=list(s[0])
print(b)'''

input_string=list(input().split())
first=[]
second=[]
first=list(input_string[0])
second=list(input_string[1])
n=int(input_string[2])
for i in range(0,len(first)):
    for j in range(0,len(second)):
        if first[i]==second[j]:
            first.pop(i)
            second.pop(i)
if len(first) and len(second)== n:
    print("yes")
else:
    print("no")
    
