from src.Solution import Solution
from ..utils import string_to_int_arr
from ..Solution import Solution 

class P2(Solution):
    # Given the arguments as an array of string transform it to the correct format. 
    @staticmethod
    def get_arguments(args):
        arg0 = args[0]
        return [arg0]

    @staticmethod 
    def format_result(result): 
        return "{0}\n".format(result)

    @staticmethod
    def solve(s: str) -> str:
        def recursive(s, i): 
            curr_s = ""

            while i < len(s):
                l = s[i]
                if isInteger(l):
                    sequence, i = getSequence(s, i)
                    curr_s += sequence
                else: 
                    curr_s += l
                i += 1
                    
            return curr_s
    
        def getSequence(s, pos):
            repeats, start = getFullInteger(s, pos)
            string, end = getString(s, start+1, repeats)
            return (string, end)
        
        # returns the last position of the integer and the integer
        def getFullInteger(s, pos):
            integer = ""
            while isInteger(s[pos]):
                integer += s[pos]
                pos+=1
                
            return (int(integer), pos)
        
        def isInteger(letter):
            return ord('0') <= ord(letter) and ord('9') >= ord(letter)

        def getString(s, start, repeats):
            curr_s = ""
            i = start
            while i < len(s):
                if s[i] == "]":
                    return (repeats*curr_s, i)
                elif isInteger(s[i]):
                    sequence, i = getSequence(s, i)
                    curr_s += sequence
                else: 
                    curr_s+= s[i]
                i+=1
                    
            return ("", 0)

        i = 0

        return recursive(s, i)