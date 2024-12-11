N = int(input())
dic = {}
for i in range(N):
    ent = str(input()).split()
    dic.__setitem__(ent[0],ent)         #NOTE - add new item to the dictionary
inp = input()
out = []
for word in inp.split():
    c=0                             #NOTE - counter to indicate  if the word is defined in my dictionary or not
    for cat in list(dic.values()):          #NOTE - iterate over dictionary values
        if cat.count(word) != 0:
            ind = cat.index(word)           #NOTE - unnecessary line to know the language of input
            out.append(cat[0])              #NOTE - add translation to output
            break
        c+=1
    if c == N:
        out.append(word)                    #NOTE - if the word is not defined in the dictionary, add the original word as the output

for p in out:
    print(p,end=" ")