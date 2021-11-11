from algpy.recursion.binary_search import binary_search

list_to_search = [1, 8, 15, 22, 29, 36, 37, 41, 44]

print(str(binary_search(list_to_search, 22, 0, len(list_to_search) - 1)))
print(str(binary_search(list_to_search, 23, 0, len(list_to_search) - 1)))