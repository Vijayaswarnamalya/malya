input_size=input()
list1=list(map(int,input_size.split()))
k=list1[1]
n_value=list(map(int,input().split()))
k_value=list(map(int,input().split()))
for i in range(0,k):
    n_value.append(k_value[i])
    print(max(n_value),end=' ')
