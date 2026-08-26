# expand a given number 5601 into 5000 + 600 + 1

def expanded_form(num):


    decimals = list(str(num))
    output_numbers = []
    for i, decimal in enumerate(decimals):
        output_numbers.append(int(decimal) * (10 ** (len(decimals)-i-1)))
        
    output = ""
    for element in output_numbers[:-1]:
        if element == 0:
            continue
        output += f"{element} + "

    if output_numbers[-1] != 0:
        output += f"{output_numbers[-1]}"
    if output_numbers[-1] == 0:
        output = output[:-2]
    output = output.rstrip()
    return output

test = 405801
print(expanded_form(test))
print("script finished")

# better: use  ' + '.join(str(element) for element in output_numbers if element != 0) after constructing output_numbers