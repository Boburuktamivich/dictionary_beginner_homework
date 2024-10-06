def find_length_of_values(data: dict) -> int:
    """
    Return the sum of the length of all values in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The sum of the length of all values in the dictionary.
    """
    i = 0
    c = 0
    v = list(data.values())

    while i <len(v):
        c += len(v[i])
        i += 1
    return c
result = find_length_of_values({
    1 : "Khiva", 
    2 : "Namangan", 
    3 : "Samarkand", 
    4 : "Tashkent"
  })
print(result)