n1=float(input())
op=input()
n2=float(input())

if op=="+":
    print(n1,op,n2,"=",n1+n2)
elif op=="-":
    print(n1,op,n2,"=",n1-n2)
elif op=="*":
    print(n1,op,n2,"=",n1*n2)
elif op=="/":
    print(n1,op,n2,"=",n1/n2)
else:
    print("NÃO FOI POSSIVEL REALIZAR A OPRAÇÃO!")
