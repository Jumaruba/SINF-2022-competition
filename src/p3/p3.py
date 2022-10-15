from src.Solution import Solution
from ..Solution import Solution 

class P3(Solution):
    @staticmethod 
    def get_arguments(args):
        arg0 = args[0]
        ratings = [list(map(int, arg0.split(" ")))]
        return ratings

    @staticmethod
    def format_result(result):
        return str(result) + "\n"

    @staticmethod
    def solve(ratings: list) -> int: 
      
        result = [] 
        result = [1 for i in enumerate(ratings)]
        ratingsSize = len(ratings) 
        
        def updateRightToLeft(ratings):
            nonlocal result
            nonlocal ratingsSize
            for i in range(1, ratingsSize): 
                if ratings[i] > ratings[i-1] and result[i] <= result[i-1]:
                    result[i] = max(result[i-1] + 1, result[i]+1)
                    
        def updateLeftToRight(ratings):
            nonlocal result 
            nonlocal ratingsSize
            for i in range(ratingsSize-2, -1, -1): 
                if ratings[i] > ratings[i+1] and result[i] <= result[i+1]:
                    result[i] = max(result[i+1] +1, result[i]+1)
       
        
        updateRightToLeft(ratings)
        updateLeftToRight(ratings)
        return sum(result)
    
    
