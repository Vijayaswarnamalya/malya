input_num=input()
list1=list(map(int,input_num.split()))
k=list1[1]
num_value=input()
num_list=list(map(int,num_value.split()))
flag=0
for i in range(0,len(num_list)-1):
	for j in range(i+1,len(num_list)):
		if num_list[i]+num_list[j]==k:
			print("yes")
			flag=1
			break
	if flag==1:
		break
if flag!=1:
	print("no")
		
