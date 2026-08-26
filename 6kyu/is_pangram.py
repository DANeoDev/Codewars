def is_pangram(st):
    check = list(st.lower())  
    alphabet = [chr(i) for i in range(ord("a"), ord("z")+1)]
    for letter in alphabet:
        if letter not in check:
            return False
    return True