'''
Implement a program, which given an integer n, computes the sum of its digits.

If a negative number is given, the function should work as if it was positive.

For example, if n is 1325132435356, the digit's sum is 43. If n is -10, the sum is 1 + 0 = 1.

In the test cases for this task we will have that -2^63 < n < 2^63.

Test examples
Input	      Output
10	             1
2	             2
-3456	        18
1325132435356	43

'''

# Solution

def digit_sum(number):
    if number < 0:
        number *= (-1)
    return(sum([int(x) for x in str(number)]))



n = 1325132435356
assert digit_sum(n) == 43

n1 = 10
assert digit_sum(n1) == 1

n2 = -10
assert digit_sum(n2) == 1

n3 = -3456
assert digit_sum(n3) == 18
