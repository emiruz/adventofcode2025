xs  = [x for x in open("input.txt","r").read().split("\n") if x]

def f(xs, i, n):
    j = i + xs[i:].index(max(xs[i:(None if n == 0 else n)]))
    if n == 0: return [xs[j]]
    return [xs[j]] + f(xs, j + 1, n + 1)

print("Part #1:", sum([int("".join(f(x, 0, -1))) for x in xs]))
print("Part #2:", sum([int("".join(f(x, 0, -11))) for x in xs]))
