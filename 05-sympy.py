from sympy import Interval, FiniteSet, Union


xs, ys = [x for x in open("input.txt","r").read().split("\n\n") if x]
xs     = [x.split("-") for x in xs.split('\n') if x]
xs     = sorted(list(set((int(a), int(b)) for a,b in xs)))
ys     = [int(y) for y in ys.split('\n') if y]
cnt    = lambda x: sum(1 for (a,b) in xs if a <= x <= b)
xs1    = Union(*[Interval(a,b) for a,b in xs]).args

print("Part #1:", sum(1 for y in ys if cnt(y) > 0))
print("Part #2:", sum(len(x) if isinstance(x,FiniteSet) else 1+x.end-x.start for x in xs1))
