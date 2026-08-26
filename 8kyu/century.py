def century(year):
    almost_century = int(year / 100)
    if almost_century > 0:
        if (year/100).is_integer():
            return almost_century
    return almost_century + 1
    
    
test = 1651
almost_century = int(test / 100)
print((test/almost_century).is_integer())
print(almost_century)
print(century(test))
print("script finished")
