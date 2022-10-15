def is_int(l: str):
        return ord(l) >= ord('0') and ord(l) <= ord('9') 



    

# Transforms a string array such as "[1,2,3,4]" in a array of ints: [1,2,3,4]
# Or even "[[1,2],[2,3]]" in [[1,2],[3,4]]
def string_to_int_arr(arr_string, first=True): 
    result = []
    arr_size = len(arr_string)
    i = 1

    while i < arr_size: 
        checked_int = False 
        l = arr_string[i]
        if l == "[":
            inner_arr, last_pos = string_to_int_arr(arr_string[i:], False)
            result.append(inner_arr)
            i += last_pos + 1 
        if l == "]":
            break

        n = ""
        while is_int(l):
            checked_int = True 
            n += l 
            i += 1
            l = arr_string[i] 

        if not checked_int: 
            i += 1
        else: 
            result.append(int(n))

    if first:
        return result 
    else: 
        return (result, i)


        

