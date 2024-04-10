def expand_strings(input_list):
    expanded_list = []
    for item in input_list:
        for digit in range(10):
            new_item = item.replace('x', str(digit))
            expanded_list.append(new_item)
    return expanded_list

input_list = [
    "95960x7653",
    "96220x7653",
    "97970x7653",
    "99060x7653",
    "95961x7653",
    "96221x7653",
    "97971x7653",
    "99061x7653",
    "95962x7653",
    "96222x7653",
    "97972x7653",
    "99062x7653",
    "95963x7653",
    "96223x7653",
    "97973x7653",
    "99063x7653",
    "95964x7653",
    "96224x7653",
    "97974x7653",
    "99064x7653",
    "95965x7653",
    "96225x7653",
    "97975x7653",
    "99065x7653",
    "95966x7653",
    "96226x7653",
    "97976x7653",
    "99066x7653",
    "95967x7653",
    "96227x7653",
    "97977x7653",
    "99067x7653",
    "95968x7653",
    "96228x7653",
    "97978x7653",
    "99068x7653",
    "95969x7653",
    "96229x7653",
    "97979x7653",
    "99069x7653",
    "84910x7653",
    "84920x7653",
    "84930x7653",
    "84940x7653",
    "84918x7653",
    "84928x7653",
    "84938x7653",
    "84919x7653",
    "84929x7653",
    "84939x7653"
]


expanded_list = expand_strings(input_list)

with open('expanded_numbers.txt', 'w') as f:
    for item in expanded_list:
        f.write("%s\n" % item)
