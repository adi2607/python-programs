def palindrome(int):
    rev_num=int[::-1]
    return int==rev_num

num=input("Enter Number: ")
if palindrome(num):
    print(f"{num} is palindrome")
else:
    print(f"{num} is not palindrome")