def sum_even_values(data: dict) -> int:
    '''
    Return the sum of all even values in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The sum of all even values in the dictionary
    '''
    i = 0
    s = 0
    v = list(data.values())
    while i <len(data):
        if v[i] % 2 == 0:
            s += v[i]
        i += 1
    return s
result = sum_even_values(
    {
    1: 22, 
    2: 3.5, 
    4: 1, 
    6: 7, 
    5: 2, 
    7: 3
  }
)
print(result)