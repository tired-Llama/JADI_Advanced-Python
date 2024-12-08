#NOTE - well I think every thing is clear enough
n = int(input())
entery = []
for i in range(n):
    entery.append(input().split('.'))

for i in entery:
    n = entery.index(i)
    entery[n][1] = str(entery[n][1]).capitalize()
entery.sort()
for i in entery:
    print(i[0],i[1],i[2])