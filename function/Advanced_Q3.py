def flatten_list(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):  # Check if the item is a list
            flat_list.extend(flatten_list(item))  # Recursively flatten the sublist
        else:
            flat_list.append(item)  # If not a list, add the item directly
    return flat_list