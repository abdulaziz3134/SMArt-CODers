n=int(input("enter N :  "))
sum=0
odd=0
for i in range(1,n+1):
    if i%2==0:
        sum=sum+i
    else:
        odd=odd+i
print("the sum of even numbers: ",sum)
print("the sum of odd numbers: ",odd)            