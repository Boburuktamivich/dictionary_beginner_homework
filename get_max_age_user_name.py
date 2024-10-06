def get_max_age_user_name(data:list) -> str:
    """
    Return the name of the user with the maximum age in a dictionary.

    Args:
        data (dict): A dictionary of values
    Returns:
        str: The name of the user with the maximum age in the dictionary
    """
    i = 0
    ls = []
    while i <len(data):
        ls.append(data[i]['age'])
        i += 1
    return max(ls)
result = get_max_age_user_name(
    [{'name': 'John', 'age': 27},
     {'name': 'Marry', 'age': 42}]
)
print(result)