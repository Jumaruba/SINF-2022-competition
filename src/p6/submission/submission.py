result = []
res = []
args_size = int(input())
for i in range(args_size):
    res.append(list(map(int, input().split(" ")))) 
trees = res 

def get_determinant(p1, p2, p3): 
    return p2[0]*p3[1] + p3[0]*p1[1]+p1[0]*p2[1]-p2[0]*p1[1]-p1[0]*p3[1]-p3[0]*p2[1]

def add_result(): 
    for i, p in enumerate(trees):
        appended = False
        if len(result) <= 1: 
            result.append(p)
            continue 
        while get_determinant(result[-2], result[-1], p) < 0: 
            result.pop() 
            if len(result) < 2: 
                result.append(p)
                appended = True
                break 

        if not appended and len(result) >= 2 and get_determinant(result[-2], result[-1], p) >= 0: 
            result.append(p)

# Get lower fence
trees.sort()
add_result()

# Get upper fence
trees = sorted(trees, key=lambda x: (-x[0], -x[1]))
add_result()

result = set([(x[0], x[1]) for x in result])
result = list(sorted(result))

for i in result:
    print("{} {}".format(i[0], i[1]))

            
            