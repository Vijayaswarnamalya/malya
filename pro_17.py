alp=input()

a=list(map(int,alp.split()))

k=a[1]
h=input()

s=list(map(int,h.split()))
flag=0
for i in range(0,len(s)-1):
	for j in range(i+1,len(s)):
		if s[i]+s[j]==k:
			print("yes")
			flag=1
			break
	if flag==1:
		break
if flag!=1:
	print("no")
		
