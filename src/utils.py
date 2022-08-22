# Transforms a string array such as "[1,2,3,4]" in a array of ints: [1,2,3,4]
def string_to_int_arr(arr_string): 
    return [int(x) for x in list(arr_string[1:-2].split(","))]
 