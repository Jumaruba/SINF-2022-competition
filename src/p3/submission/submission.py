arg0 = input()
ratings = list(map(int, arg0.split(" ")))
result = [] 
result = [1 for i in enumerate(ratings)]
ratingsSize = len(ratings) 

def updateRightToLeft(ratings, result, ratingsSize):
    for i in range(1, ratingsSize): 
        if ratings[i] > ratings[i-1] and result[i] <= result[i-1]:
            result[i] = max(result[i-1] + 1, result[i]+1)
    return [result, ratingsSize]

def updateLeftToRight(ratings, result, ratingSize):
    for i in range(ratingsSize-2, -1, -1): 
        if ratings[i] > ratings[i+1] and result[i] <= result[i+1]:
            result[i] = max(result[i+1] +1, result[i]+1)
    return [result, ratingsSize]


[result, ratingsSize] = updateRightToLeft(ratings, result, ratingsSize)
[result, ratingsSize] = updateLeftToRight(ratings, result, ratingsSize)
print(sum(result))