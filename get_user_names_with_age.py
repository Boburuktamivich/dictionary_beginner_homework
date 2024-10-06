def get_user_names_with_age(data:list, age:int) -> list:
    """
    Return a list of users with a given age

    Args:
        data (dict): A dictionary of values
        age (int): The age to search for
    Returns:
        list: A list of users with the given age
    """
    i = 0
    ls = []
    while i <len(data):
        if data[i]['age'] == age:
            ls.append(data[i]['name'])
        i += 1
    return ls
result = get_user_names_with_age(
    [{
    'name': 'John', 
    'age': 30
  }, 
  {
    'name': 'Ann', 
    'age': 32
  }, 
  {
    'name': 'Sam', 
    'age': 27
  }, 
  {
    'name': 'Mary', 
    'age': 32
  }], 32)
print(result)