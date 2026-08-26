def longest_consec(strarr, k):
    if k < 1 or strarr==[] or k>len(strarr):
        return ""    
    concats = []
    i = 0 
    for i in range(0, len(strarr) -k +1):
        concats.append("".join(strarr[i:i+k]))
        
    return max(concats, key=len)


test=["test", "ab", "cde", "fgh"]


print(longest_consec(test, 2))



