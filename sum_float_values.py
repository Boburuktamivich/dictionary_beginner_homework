def sum_float_values(data: dict) -> float:
    '''
    Return the sum of all float values in dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        float: The sum of all float values in the dictionary.
    '''
    i = 0
    s = 0
    v = list(data.values())
    while i <len(data):
        if type(v[i]) == float:
            s += v[i]
        i += 1
    return s
result = sum_float_values(
    {1: 22.4, 
    2: 3.5, 
    4: 1, 
    6: 7.6, 
    5: 2, 
    7: 3
  }
)
print(result)