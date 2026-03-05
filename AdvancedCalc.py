Number1 =float(input("Enter First Number: "))
Number2 = float(input("Enter Second Number: "))
Veriable= input("Choose your veriable +,-,*,/: ")
if Veriable=="+":
    print(Number1 + Number2)
elif Veriable=="-":
    print(Number1-Number2)
elif Veriable=="*":
    print(Number1*Number2)
elif Veriable=="/" and Number2==0 and Number1==1:
    print("Undefined")
elif Veriable=="/":
    print(Number1/Number2)

