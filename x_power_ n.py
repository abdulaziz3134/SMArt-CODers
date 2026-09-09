x=int(input("enter the base: "))
n=int(input("enter the power: "))
pow=1
print("result")
for i in range(1,n+1):
    pow=pow*x
    print(i,".",pow)   