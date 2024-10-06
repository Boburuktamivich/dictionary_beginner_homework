def sum_dict_values(data: dict) -> int:
    '''
    Return the sum of all values in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The sum of all values in the dictionary
    '''
    i = 0
    s = 0
    v = list(data.values())
    while i < len(data):
        s += v[i]
        i += 1
    return s
result = sum_dict_values(
    {1: 23, 
    2: 3.5, 
    4: 1, 
    6: 7, 
    5: 2, 
    7: 3}
)
print(result)