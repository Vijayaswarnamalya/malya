input_data=input()
list1=input_data.split(" ")
num1=int(list1[0])
num2=int(list1[1])
maximum=max(num1,num2)
while(1):
    if(maximum%num1==0 and maximum%num2==0):
        print(maximum)
        break
    maximum+=1
