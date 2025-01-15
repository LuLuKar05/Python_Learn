string = "Hello#WOrld#####hi"  # Renamed to avoid using 'str' (a Python keyword)
split_list = string.split("#")  # Split the string by '#'

# Remove empty strings
filtered_list = [item for item in split_list if item != '']  # List comprehension for filtering
# filtered_list = []
# for item in split_list:  # Iterate through split_list
#     if item != '':  # Check if item is not an empty string
#         filtered_list.append(item)  # Add the item to the new list
print(item)
print(filtered_list)  # Output the result
