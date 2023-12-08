def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high)//2
        guess = list[mid]

        if guess == item:
            return mid

        if guess > item:
            high = mid - 1

        else:
            low = mid + 1

    return None


my_list = [1, 3, 5, 8, 9, 12, 10, 11, 31, 25]
my_list = sorted(my_list)
print(my_list)

print(binary_search(my_list, 25))
