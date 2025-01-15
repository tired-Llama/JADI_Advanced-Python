from statistics import mean
class School:
    def __init__(self):
        self.population = int(input())
    
    def set_age(self):
        self.age = list(map(lambda x: float(x),input().split(sep=" ")))
    def set_height(self):
        self.height = list(map(lambda x: float(x),input().split(sep=" ")))
    def set_weight(self):
        self.weight = list(map(lambda x: float(x),input().split(sep=" ")))

    
    def describe(self):
        print(mean(self.age))
        print(mean(self.height))
        print(mean(self.weight))
    
    def info(self):
        return [mean(self.height), mean(self.weight)]

def compare(a,b):
    A = a.info()
    B = b.info()
    if A[0] == B[0]:
        if A[1] == B[1]:
            print("Same")
        elif A[1] > B[1]:
            print("B")
        else:
            print("A")
    elif A[0] > B[0]:
        print("A")
    else:
        print("B")

# this section runs the program
a = School()
a.set_age()
a.set_height()
a.set_weight()
b = School()
b.set_age()
b.set_height()
b.set_weight()
a.describe()
b.describe()
compare(a,b)