xs, ys = [x for x in open("input.txt","r").read().split("\n\n") if x]
xs     = [x.split("-") for x in xs.split('\n') if x]
xs     = sorted(list(set((int(a), int(b)) for a,b in xs)))
ys     = [int(y) for y in ys.split('\n') if y]
cnt    = lambda x: sum(1 for (a,b) in xs if a <= x <= b)

def merge(xs):
    ys, (x0, x_) = [], xs[0]
    for i in range(1, len(xs)):
        next_x0, next_x_ = xs[i]
        if x_ >= next_x0:
            x_ = max(x_, next_x_)
        else:
            ys.append((x0, x_))
            x0, x_ = next_x0, next_x_
    ys.append((x0, x_))
    return ys

print("Part #1:", sum([1 for y in ys if cnt(y) > 0]))
print("Part #2:", sum(1+b-a for a,b in merge(xs)))
