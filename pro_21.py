n_div=int(input())
num_list=list(map(int,input().split()))
n_div1=num_list[:n_div//2]
n_div2=num_list[n_div//2:]
if sum(n_div1)//len(n_div1) == sum(n_div2)//len(n_div2):
    print("yes")
    exit()
print("no")
    
