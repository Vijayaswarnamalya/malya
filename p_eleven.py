num=input()
list1=num.split(" ")
#day_list=['Monday','Tuesday','Wednesday','Thursday','Friday']
weekend_list=['Sunday','Saturday']
for i in range(0,len(list1)):
    if list1[i] in weekend_list:
        print("yes")
    else:
        print("no")
