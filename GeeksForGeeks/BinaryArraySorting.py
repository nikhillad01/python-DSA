"""
Problem Link: https://practice.geeksforgeeks.org/problems/binary-array-sorting/0
Given a binary array, sort it in non-decreasing order
Input: First line contains an integer denoting the test cases 'T'.  Every test case contains two lines, first line is size and
second line is space separated elements of arra
Output:  Space separated elements of sorted arrays.  There should be a new line between output of every test case.
Input:
2
5
1 0 1 1 0
10
1 0 1 1 1 1 1 0 0 0
Output:
0 0 1 1 1
0 0 0 0 1 1 1 1 1 1
"""

if __name__ == '__main__':
    tests = int(input("Enter number of test cases to run : "))
    numbers = int(input('Enter binary numbers '))
    arr = [int(x) for x in str(numbers)]
    print(arr)
    # position = -1
    for i in range(len(arr)):
        if arr[i] > arr[i+1]:
            arr[i + 1] = arr[i]

    print(arr)