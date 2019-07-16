alp=int(input())
lst=[]
for i in range(alp):
    n=input()
    a=list(map(int,n.split()))
    lst=lst+a
lst.sort()
for i in lst:
    print(i,end=" ")

