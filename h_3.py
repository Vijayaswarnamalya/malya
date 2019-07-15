number=int(input())
number_input=input()
list1=list(map(int,number_input.split()))
for i in range(0,len(list1)):
    if i == list1[i]:
        print(list1[i],end=' ')
    
