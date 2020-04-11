"""
You are given an integer input N and you have to find whether it is Anshuman’s favourite or not.
If it is then print “YES” else print “NO”.
A number is Anshuman’s favourite if it is either the sum or the difference of the integer 5. (5+5, 5+5+5, 5-5,5-5-5+5+5…..)
Input:
The first line of input contains an integer denoting the number of test cases . Next line of input contains an integer N to be tested.
Output:
For each test case , the output is in a new line containg the answer 'YES' or 'NO' depending on whether the given number N is Anshuman's favourite or not .
Constraints:
1<=T<=100
-10^9<=N<=10^9
Example:
Input :
1
10
Output :
YES
Because 10 can be written as a sum of 5+5.
Example:
Input :
1
9
Output :
NO
Input :
2
-255
389
Output :
YES
NO
"""


def favourite_number():
    try:
        tests = int(input("Enter number of tests "))
    except:
        print('please add valid integer ')
        return
    while tests > 0:
        try:
            num = int(input("Enter number to if it is anshumans favouite"))
        except:
            print('please add valid integer ')
            return
        if (num % 5 == 0):
            print("Yes , the number is anshumans favourite")
        else:
            print("No")


favourite_number()
