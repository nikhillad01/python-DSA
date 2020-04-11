"""
Check if count of Alphabets and count of Numbers are equal in the given String
"""

if __name__ == '__main__':
    str = input("Enter string with numbers:   ")

    int_count = 0
    char_count = 0
    for letter in str:
        if ord(letter) in range(48, 58):
            int_count += 1
        elif ord(letter) in range(65, 91) or ord(letter) in range(97, 123):
            char_count += 1

    if int_count == char_count:
        print('Yes')
    else:
        print('No')
    print('Integer counts in string ', int_count)
    print('char count in string', char_count)
