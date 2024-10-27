def calculate_structure_sum(a):
    vsego = 0
    for element in a:
        if isinstance(element, int):
            vsego += element
        elif isinstance(element, str):
            vsego += len(element)
        elif isinstance(element, (list, tuple)):
            vsego += calculate_structure_sum(element)
        elif isinstance(element, dict):
            for key , value in element.items():
                vsego += calculate_structure_sum([key, value])

    return vsego







data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
