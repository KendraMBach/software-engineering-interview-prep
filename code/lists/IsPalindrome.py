'''
A palindrome is а word or a phrase or a number, that when reversed, stays the same.

For example, the following sequences are palindromes : "azobi4amma4iboza" or "anna".

But this time, we are not interested in words but numbers. A "number palindrome" is a number, that taken backwards, remains the same.

For example, the numbers 1, 4224, 9999, 1221 are number palindromes.

Implement a function, which given an integer computes if it's a palindrome.

Input
One integer n, where 0 < n <= 10,000,000,000.

Output
Your function must return a boolean true if n is a palindrome and false otherwise.

Test examples
Input	Output
1	true
42	false
100001	true
999	true
123	false

'''
#Solution

def is_numeric_palindrome(n):
    if n <= 9:
        return True
    n = str(n)
    i = 0
    j = len(n) - 1

    while i <= j:
        if int(n[i]) == int(n[j]):
            i+=1
            j-=1
            continue
        else:
            return False
    return True


n = 100
assert not is_numeric_palindrome(n)

n=42
assert not is_numeric_palindrome(n)

n=1
assert is_numeric_palindrome(n)

n=100001
assert is_numeric_palindrome(n)

n=999
assert is_numeric_palindrome(n)
