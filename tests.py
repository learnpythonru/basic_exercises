from collections  import defaultdict
d = defaultdict(list)
for i in range(5):
    d[i].append(i)
print(d)    