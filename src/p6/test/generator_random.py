import random 

def get_unique_pair(s): 
    n1 = random.randint(0,100)
    n2 = random.randint(0,100)

    while (n1, n2) in s:
        n1 = random.randint(0,100)
        n2 = random.randint(0,100)

    return [s, n1, n2]



n = random.randint(1, 3000)
print(n)
s:set = set([])
for i in range(n):
    [s, n1, n2] = get_unique_pair(s)
    s.add((n1,n2))  
    print("{} {}".format(n1, n2))
