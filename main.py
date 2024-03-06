def is_palindrome(n):
    if n == n[::-1]:
        print(f"{n} is a palindrome!")
    else:
        print(f"{n} is not a palindrome!")

string = input("Enter a string: ").lower()
is_palindrome(string)
