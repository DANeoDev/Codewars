def alphabet_position(text):
    let_nums=""
    for letter in text.lower():
        if 97 <= ord(letter) <= 122:
            let_nums +=f" {ord(letter)-96}"
    return let_nums

text ="az"
print(alphabet_position(text))