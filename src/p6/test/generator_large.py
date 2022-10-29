import random 

def get_unique_pair(s): 
    n1 = random.randint(0,100)
    n2 = random.randint(0,100)

    while (n1, n2) in s:
        n1 = random.randint(0,100)
        n2 = random.randint(0,100)

    return [s, n1, n2]



s:set = set([])
print(3000)
for i in range(3000):
    [s, n1, n2] = get_unique_pair(s)
    s.add((n1,n2))  
    print("{} {}".format(n1, n2))
