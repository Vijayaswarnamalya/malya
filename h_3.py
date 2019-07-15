number=int(input())
number_input=input()
list1=list(map(int,number_input.split()))
l=-1
flag=0
for i in range(0,len(list1)):
    if i == list1[i]:
        flag=1
        print(list1[i],end=' ')
if flag!=1:
    print(l)
        
    
