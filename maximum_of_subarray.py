if __name__ == '__main__':
    testCases = int(input("Enter number of test cases "))

    while testCases > 0:
        k = 0
        array = input("Enter numbers with spaces ")
        size = (input("Size of subarray"))
        array = array.split(" ")
        for i in range(k, len(array)):
            subArray = array[k:k + int(size)]
            if len(subArray) == size:
                print(max(subArray))
                k = k + 1
        testCases = testCases - 1
