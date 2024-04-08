# How to Remove the None values from a Dictionary in Python

my_dict = {
    'name': 'Bobby Hadz',
    'age': None,
    'country': None,
    'language': 'German'
}

new_dict = {
    key: value for key, value in my_dict.items()
    if value is not None
}

# 👇️ {'name': 'Bobby Hadz', 'language': 'German'}
print(new_dict)