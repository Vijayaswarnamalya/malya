input_list=list(map(int,input().split()))
x=input_list[0]
y=input_list[1]
def gcd_func(x,y):
    if y==0:
        print(x)
    else:
        gcd_func(y,x%y)
gcd_func(x,y)
