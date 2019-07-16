input_val=int(input())
lst=[]
for i in range(input_val):
    value=input()
    a=list(map(int,value.split()))
    lst=lst+a
lst.sort()
for i in lst:
    print(i,end=" ")
