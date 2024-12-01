my_list = list(map(int, input("Enter numbers separated by spaces: ").split()))
unique_list = remove_duplicates(my_list)
print("List after removing duplicates:", unique_list)