# # def maxSum(arr, n, k):
#     # k must be greater
#     if (n < k):
#         print("Invalid")
#         return -1
#
#     # Compute sum of first
#     # window of size k
#     res = 0
#     for i in range(k):
#         res += arr[i]
#     print(res,'first')
#         # Compute sums of remaining windows by
#     # removing first element of previous
#     # window and adding last element of
#     # current window.
#     curr_sum = res
#     for i in range(k, n):
#         print('k,n',arr[i],arr[i - k])
#         curr_sum += arr[i] - arr[i - k]
#         print(i - k),
#         res = max(res, curr_sum)
#
#     return res
# a=(1,3,'a')
# print(a)
#
# # Driver code
# # arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
# # k = 3
# # n = len(arr)
# # print(maxSum(arr, n, k))
# #
# arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
# k = 4
# n = len(arr)
# maxSum(arr, n, k)
# #
# # def listComp():
# #     number_list = [x for x in range(20) if x % 2 == 0]
# #     print(number_list)
# #     return number_list
# # # print(listComp())
# # This code is contributed by Anant Agarwal.
#
#
#
#
# def jump_code(array):
#     reachable = 0
#
#     for i in range(0,len(array)):
#         if reachable < i:
#             return False
#         print('i',i,'arr[i]',array[i])
#         print('i+array[i]',i+array[i])
#         reachable = max(reachable,i+array[i])
#         print('reachable',reachable)
#     return True
#
#
#
def twos_sum(target,nums):
        # def cntArray(A, N):

    # Initialize result with 0
    result = 0

    for i in range(0, N):

        # All size 1 sub-array
        # is part of our result
        result = result + 1

        # Element at current index
        current_value = A[i]

        for j in range(i + 1, N):

            # Check if A[j] = A[i]
            # increase result by 1
            if (A[j] == current_value):
                result = result + 1

    # Print the result
    print(result)
    print("\n")

# Driver code
A = [1, 2, 1, 5, 2,3,1,3]
N = len(A)

# cntArray(A, N)


print(twos_sum(A, N))
# # print(jump_code([3,2,1,0,4]))
#
#
#
#
