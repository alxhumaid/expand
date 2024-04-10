def expand_strings(input_list):
    expanded_list = []
    for item in input_list:
        for digit in range(10):
            new_item = item.replace('x', str(digit))
            expanded_list.append(new_item)
    return expanded_list

input_list = [
   
]


expanded_list = expand_strings(input_list)

with open('expanded_numbers.txt', 'w') as f:
    for item in expanded_list:
        f.write("%s\n" % item)
