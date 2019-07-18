def rever(strings):
    return [x[::-1] for x in strings]
list1=[]
list1=rever(input_string)
s=[str(i) for i in list1]
result=" ".join(s)
print(result) 
