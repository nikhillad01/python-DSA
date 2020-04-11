"""Given an array arr[] of n elements, write a function to search a given element x in arr[]."""
# The time complexity of above algorithm is O(n).
if __name__ == '__main__':
    array = [1, 2, 3, 4, 6, 7, 9, 5, 31, 11, 4, 6, 8, 100, 193, 283, 5839, 2345, '23424342', 233333]
    x = int(input("Enter element to search : "))
    for i in range(0, len(array)):
        if array[i] == x:
            print('Element found at position ', i)
            break
