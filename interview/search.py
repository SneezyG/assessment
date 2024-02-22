
"""
--- ALGORITHM:
--- The recursive searching algorithm takes a list and a target number as inputs. It checks if the starting index is beyond the list length, if so, it returns False. If the element at the current index matches the target, it returns True. Otherwise, it recursively calls itself with the next index until the end of the list is reached.
"""



def recursive_search(arr, target, index=0):
    if index >= len(arr):
        return False
    elif arr[index] == target:
        return True
    else:
        return recursive_search(arr, target, index + 1)


numbers = [1, 3, 5, 7, 9]
target_number = int(input("Enter a number to search for: "))
result = recursive_search(numbers, target_number)

if result:
    print(f"{target_number} found in the list.")
else:
    print(f"{target_number} not found in the list.")
