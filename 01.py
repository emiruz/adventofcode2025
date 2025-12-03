from itertools import accumulate


xs  = [x for x in open("input.txt","r").read().split() if x]
xs  = [int(x.replace("L","-").replace("R","")) for x in xs]
xs1 = list(accumulate([50] + xs, lambda a, b: (a + b) % 100))
xs2 = [abs(x) // 100 for x in xs]
xs  = [a + 100 * b * (1 if a < 0 else -1) for a, b in zip(xs, xs2)]
xs3 = [1 for a, b in zip(xs1, xs) if (a > 0 and a + b < 0) or a + b > 100]

print("Part 1:", xs1.count(0), "Part 2:", sum(xs3) + sum(xs2) + xs1.count(0))
