def find_int_keys(data: dict) -> list:
    """
    Return a list of all keys in a dictionary that are integers.
    Args:
        data (dict): A dictionary of values
    Returns:
        list: A list of all keys in the dictionary that are integers.
    """
    i = 0
    ls = []
    keys = list(data.keys())
    
    while i < len(keys):
        if type(keys[i]) == int: 
            ls.append(keys[i])
        i += 1  
    return ls 
result = find_int_keys({ 'a': 1, 3: 2, 'b': 7, 12: 'R' })
print(result)