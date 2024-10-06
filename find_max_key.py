def find_max_key(data: dict):
    """
    Return the maximum int or float key in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The maximum key in the dictionary.
    """
    key = list(data.keys())
    return max(key)
result = find_max_key({1: 'a', 2: 'b', 3: 'c'})
print(result)