input_num=int(input())
sum = 0  
temp = input_num  
while temp > 0:  
   digit = temp % 10  
   sum += digit ** 2  
   temp //= 10
print(sum)
