from itertools import chain


xs  = [x.strip().split("-") for x in open("input.txt","r").read().split(",")]
xs  = chain(*[range(int(a), int(b) + 1) for a, b in xs])
xs  = [str(x) for x in xs]
ys  = [len(x)//2 for x in xs]
rep = lambda x: next((int(x) for i in range(1, (len(x)//2)+1) if x[:i]*(len(x)//i)==x), 0)

print("Part #1:", sum([int(x) for x, y in zip(xs, ys) if x[y:] == x[:y]]),
      "Part #2:", sum([rep(x) for x in xs]))
