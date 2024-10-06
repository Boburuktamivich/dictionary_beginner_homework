def find_max_value(data: dict):
    """
    Return the maximum int or float value in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The maximum value in the dictionary.
    """
    v = list(data.values())
    return max(v)
result = find_max_value({'a': 1, 'b': 2, 'c': 3})
print(result)