from functools import reduce
import re


x0 = open("input.txt","r").read()
xs = [x for x in x0.split("\n") if x]
xs = [[y for y in re.split(" +", x) if y] for x in xs]
op = lambda a,b,c: int(a)*int(b) if c=="*" else int(a)+int(b)
p1 = sum(reduce(lambda a, b: op(a,b, x[-1]), x[:-1]) for x in list(zip(*xs)))

xs = [list(x) for x in x0.split("\n") if x]
xs = list(zip(*xs))[::-1]
xs = [[y for y in x if y != ' '] for x in xs]

def calcs(xs):
    stack = []
    for x in filter(None, xs):
        if x[-1] in ["*","+"]:
            stack.append(int("".join(x[:-1])))
            yield reduce(lambda a,b: op(a,b,x[-1]), stack)
            stack.clear()
        else:
            stack.append(int("".join(x)))

print("Part #1:", p1, "Part #2:", sum(calcs(xs)))
