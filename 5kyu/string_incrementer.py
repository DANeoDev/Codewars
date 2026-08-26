def increment_string(string):
    endnum_in_string=[]
    for el in reversed(string):
        if el.isdigit():
            endnum_in_string.append(el)
        else: 
            break
    print(endnum_in_string)

    leading_zeroes=0
    for el in reversed(endnum_in_string):
        if int(el) == 0:
            leading_zeroes+=1
        else:
            break    

    print(leading_zeroes)

    if leading_zeroes>0:
        clean_endnum_in_string=endnum_in_string[:-(leading_zeroes)]
    else:
        clean_endnum_in_string=endnum_in_string

    print(clean_endnum_in_string)

    if len(endnum_in_string) > 0:
        clean_string=string[:-len(endnum_in_string)]
    else:
        clean_string=string    

    print(clean_string)

    if clean_endnum_in_string==[]:
        return clean_string + (leading_zeroes-1)*"0" +"1"

    for el in clean_endnum_in_string:
        if int(el) != 9:
            return clean_string + leading_zeroes*"0" + str(int("".join(reversed(clean_endnum_in_string)))+1)

    return clean_string + (leading_zeroes-1)*"0" + str(int("".join(reversed(clean_endnum_in_string)))+1)


           


test1="foo"
print(increment_string(test1))

test2="f333beer00567"
print(increment_string(test2))

