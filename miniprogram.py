import sys

line = input()
split = line.split()

left = int(split[0])
op = split[1]
right = int(split[2])

val = 0

if op == "+":
    val = left + right
elif op == "-":
    val = left - right
elif op == "*":
    val = left * right
elif op == "/":
    if right == 0:
        print("ERROR")
        sys.exit()
    val = left / right
else:
    print("Unknow")
    sys.exit()

print("{line_expr} = {val:.2f}".format(line_expr=line,val=val)) 