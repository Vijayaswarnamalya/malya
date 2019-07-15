number=int(input())
number_input=input()
list1=list(map(int,number_input.split()))
list1.sort(reverse=True)
s=[str(i) for i in list1]
result=int("".join(s))
print(result)
