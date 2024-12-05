entery = []
for i in range(10):
    entery.append(int(input()))
entery.sort()

def aya_aval(x):
    if x==1:
        return False
    state = True
    for i in range(2,x):
        if x%i == 0:
            state = False
            break
    return state

def tedad_mqsmalh_aval(x):
    addad_aval_ta = [i for i in range(1,max(entery)+1) if aya_aval(i)]
    n = 0
    for i in addad_aval_ta:
        if x%i ==0:
            n+=1
    return n
tahlil = [(tedad_mqsmalh_aval(i),i) for i in entery]
tahlil.reverse()
print(tahlil[0][1],tahlil[0][0],sep=" ")