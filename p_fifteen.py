ASCII_SIZE = 256
input_string=input()
count = [0] * ASCII_SIZE 
max = -1
c = '' 
for i in input_string: 
    count[ord(i)]+=1; 
  
for i in input_string: 
    if max < count[ord(i)]: 
        max = count[ord(i)] 
        c = i 
print(c)
