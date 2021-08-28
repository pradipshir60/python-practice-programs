No1= int (input("Enter first number"))
op= input("Enter opertor(+-/*):")
No2= int(input("Enter the second number"))

if op=="+":
    if No1==56 and No2==9 or No1==9 and No2==56:
        print(No1,"+",No2,"=77")
    else:
        result=No1+No2
        print(No1,"+",No2,"=",result)

if op=="-":
    result=No1-No2
    print(No1,"-",No2,"=",result)

if op == "*":
    if No1 == 45 and No2 == 3 or No1 == 3 and No2 == 45:
        print(No1, "*", No2, "= 555")
    else:
        result = No1 * No2
        print(No1, "*", No2, "=", result)


if op == "/":
    if No1 == 56 and No2 == 6 or No1 == 6 and No2 == 56:
        print(No1, "/", No2, "= 4")
    else:
        result = No1 / No2
        print(No1, "/", No2, "=", result)