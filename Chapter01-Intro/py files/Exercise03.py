n = int(input())
entery = []
for i in range(n):
    entery.append(input().split())

#NOTE - move all casted votes into a single list
votes = []
for i in entery:
    votes += [j for j in i[1:]]

#NOTE - sort genres on alphabetic order
genres = ['Horror', 'Romance', 'Comedy', 'History' , 'Adventure' , 'Action']
genres.sort()
#NOTE - calulate number of vote for each genre
""" at this stage, the index value of two lists refer to the same Item """
scores = [votes.count(i) for i in genres]

for i in range(max(scores),min(scores)-1,-1):       #NOTE - this loop moves from the maximum store to the minimum
    for j in range(scores.count(i)):                #NOTE - this loop repeats each score based on its repeatence
        # genres[scores.index(i)]                     #NOTE - not necessary line - find the genre corresponding to the score (remember that genre is sorted on alphabetical order)
        print(genres[scores.index(i)],":",str(i))   #NOTE - print exercise's requested output
        genres.remove(genres[scores.index(i)])      #NOTE - remove printed genre from the list
        scores.remove(i)                            #NOTE - remove printed score from the list

# genres[scores.index(3)