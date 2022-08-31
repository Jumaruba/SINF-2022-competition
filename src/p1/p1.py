from src.Solution import Solution
from ..Solution import Solution 

class P1(Solution):
    
    @staticmethod
    def get_arguments(args):
        arg0 = args[0]
        arg1 = args[1]
        return [arg0, arg1]

    @staticmethod 
    def format_result(result): 
        return "{0}\n".format(result)

    @staticmethod
    def solve(s: str, t: str):
        
        # delete all #'s of the string
        def filterString(s: str):
            s_ = ""
            for c in s: 
                if c == "#":
                    s_ = s_[:-1]
                else: 
                    s_ += c 
            return s_ 

        print(filterString(s) + ":" + filterString(t))
        return filterString(s) == filterString(t)