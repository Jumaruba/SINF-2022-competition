s = input()
t = input() 

# delete all #'s of the string
def filterString(s: str):
    s_ = ""
    for c in s: 
        if c == "#":
            s_ = s_[:-1]
        else: 
            s_ += c 
    return s_ 

print(filterString(s) == filterString(t))