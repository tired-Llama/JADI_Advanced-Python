text = input()
sentences = text.split('.')     #NOTE - split text into sentences
sentences.pop()                 #NOTE - remove the final empty string
words = [i.split() for i in sentences]      #NOTE - split each sentence into words
counter = 0
for i in words:
    for j in i:
        counter +=1
        if j.islower() == False:
            if j.isdigit() != True:
                if i.index(j) != 0:
                    j.replace(',','')
                    print(counter,':',j,sep='')