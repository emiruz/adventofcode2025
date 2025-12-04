xs   = [list(x) for x in open("input.txt","r").read().split("\n") if x]
m, n = len(xs[0])-1, len(xs)-1

def cnt(x):
    cnt, ys = 0, [-1+0j,1+0j,0-1j,0+1j,1+1j,1-1j,-1+1j,-1-1j]
    zs = [x + y for y in ys]
    zs = [(int(z.real), int(z.imag)) for z in zs if 0<=z.real<=n and 0<=z.imag<=m]
    return sum(1 for i,j in zs if xs[i][j] == "@")

def go(xs, short=False):
    ys = [complex(a,b) for a, x in enumerate(xs) for b, y in enumerate(x) if y=="@"]
    ys = [y for y in ys if cnt(y) < 4]
    if len(ys) == 0 or short: return len(ys)
    for y in ys: xs[int(y.real)][int(y.imag)] = "."
    return go(xs) + len(ys)

print("Part #1:", go(xs, True), "Part #2:", go(xs))
