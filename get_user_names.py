def get_user_names(data:list, country:str) -> list:
    """
    Return a list of users with a given country

    Args:
        data (dict): A dictionary of values
        country (str): The country to search for
    Returns:
        list: A list of users with the given country
    """
    i = 0
    ls = []
    while i < len(data):
        if data[i]['country'] == country:
            ls.append(data[i]['name'])
        i += 1
    return ls
result = get_user_names(
    [{
    'name': 'John', 
    'country': 'USA'
  }, 
  {
    'name': 'Mary', 
    'country': 'UK'
  },
  {
    'name': 'Henry', 
    'country': 'UK'
  },
  {
    'name': 'Sam', 
    'country': 'MEX'
  },
  {
    'name': 'Kevin', 
    'country': 'RUS'
  },
  {
    'name': 'Dustin', 
    'country': 'GER'
  }], 'UK')
print(result)