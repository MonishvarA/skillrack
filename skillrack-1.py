exp=input("ENTER THE EXPRESSION:")
for op in "+-*/":
    if op in exp[:-1]:
        part=exp.split(op)
        a=int(part[0])
        right=part[1].split("=")
        b=int(right[0])
        c=int(right[1])
        break
if a+b==c:
    print("+")
elif a-b==c:
    print("-")
elif a*b==c:
    print("*")
elif a/b==c:
    print("/")