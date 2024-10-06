def count_jobs(data:list, job:str) -> int:
    
    """
    Return the number of users with a given job

    Args:
        data (dict): A dictionary of values
        job (str): The job to search for
    Returns:
        int: The number of users with the given job
    """
    c = 0
    i = 0
    while i < len(data):
        if data[i]['job'] == job:
            c += 1
        i += 1
    return c

result = count_jobs([
    {'name': 'John',
    'job': 'Developer'},
    {'name': 'Mary',
    'job': 'Developer'},
], 'Developer')
print(result)