def count_users_with_age(data:list, age:int) -> int:
    """
    Return the number of users with a given age

    Args:
        data (dict): A dictionary of values
        age (int): The age to search for
    Returns:
        int: The number of users with the given age
    """
    i = 0
    c = 0
    while i < len(data):
        if data[i]['age'] == age:
            c += 1
        i += 1
    return c
result = count_users_with_age(
    [{'name':'John', 'age':27},
     {'name':'Marry', 'age':42},
     {'name':'Ann', 'age':27}], 27)
print(result) 