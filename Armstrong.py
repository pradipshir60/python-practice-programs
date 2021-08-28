num=int(input("Enter the number "))
sum=0
temp=num
while num !=0:
    r=num%10
    sum+=r**3
    num//=10

if temp==sum:
    print(temp,"is Armstrong No")
else:
    print(temp,"is not armstrong")