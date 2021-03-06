def largest_palindrome(max_factor, min_factor = 0):
    return max(palindromes(max_factor, min_factor))

def smallest_palindrome(max_factor, min_factor = 0):
    return min(palindromes(max_factor, min_factor))

def palindromes(max_factor, min_factor):
    return ((a * b, (a, b))
            for a in range(min_factor, max_factor + 1)
            for b in range(min_factor, a + 1)
            if is_palindrome(a * b))

def is_palindrome(n):
    return str(n) == str(n)[::-1]
