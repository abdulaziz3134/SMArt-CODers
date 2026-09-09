n=int(input("Enter N: "))
l=0
s=9
while n>0:
    digit= n%10
    if digit > l:
        l=digit
    if digit < s:
        s=digit
    n=n//10
print(f"largest: {l}")
print(f"smallest: {s}")    