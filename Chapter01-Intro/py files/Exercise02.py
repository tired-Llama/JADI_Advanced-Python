entery = []
for i in range(6):
    entery.append([int(i.strip()) for i in input().split("-")])

Iran = entery[:3]
Spain = [entery[0][::-1]]+entery[3:5]
Portugal = [entery[1][::-1]]+[entery[3][::-1]]+[entery[-1]]
Morocco = [entery[2][::-1]]+[entery[4][::-1]]+[entery[5][::-1]]

def calc(x):
    win = sum([1 for i in x if i[0]>i[1]])
    loss = sum([1 for i in x if i[0]<i[1]])
    draw = sum([1 for i in x if i[0]==i[1]])
    delta = sum([i[0] for i in x])-sum([i[1] for i in x])
    points = draw + 3*win
    return [win,loss,draw,delta,points]

ranking = [
    [calc(Iran)[-1],calc(Iran)[0],3,'Iran',calc(Iran)],
    [calc(Morocco)[-1],calc(Morocco)[0],2,'Morocco',calc(Morocco)],
    [calc(Portugal)[-1],calc(Portugal)[0],1,'Portugal',calc(Portugal)],
    [calc(Spain)[-1],calc(Spain)[0],0,'Spain',calc(Spain)]
]
ranking.sort()
for i in range(1,5):
    print(ranking[-i][-2], " wins:%.0f , loses:%.0f , draws:%.0f , goal difference:%.0f , points:%.0f"%tuple(ranking[-i][-1]))