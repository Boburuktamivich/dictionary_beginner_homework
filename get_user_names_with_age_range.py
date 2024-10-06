def get_user_names_with_age_range(data:list, min_age:int, max_age:int) -> list:
    """
    Return a list of users with a given age range

    Args:
        data (dict): A dictionary of values
        min_age (int): The minimum age to search for
        max_age (int): The maximum age to search for
    Returns:
        list: A list of users with the given age range
    """
    i = 0
    ls = []
    while i < len(data):
        if data[i]['age'] > max_age or data[i]['age'] < min_age:
            ls.append(data[i]['name'])
        i += 1
    return ls
result = get_user_names_with_age_range(
    [{
    'name': 'John', 
    'age': 20
  }, 
  {
    'name': 'Mary', 
    'age': 17
  },
  {
    'name': 'Ban', 
    'age': 23
  },
  {
    'name': 'John', 
    'age': 27
  }], 18, 25)
print(result)