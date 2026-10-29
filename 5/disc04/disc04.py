#Q1
def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """

    def helper(x, y):
        # Base case
        if x > m or y > n:
            return 0
        elif x == m and y == n:
            return 1
        # Recursive case
        return helper(x + 1, y) + helper(x, y + 1)
    
    return helper(1, 1)

# Solution from lectures
# Instead of updating the starting position like in my solution, they recursively update the end position by going left (n-1) and down (m-1)
def paths_solution(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    # Base case: if cannot move any further right or up
    if m == 1 or n == 1:
        return 1
    # Recursive case
    return paths(m - 1, n) + paths(m, n - 1)
    

# Q2
def max_product(s):
    """Return the maximum product of non-consecutive elements of s.

    >>> max_product([10, 3, 1, 9, 2])   # 10 * 9
    90
    >>> max_product([5, 10, 5, 10, 5])  # 5 * 5 * 5
    125
    >>> max_product([])                 # The product of no numbers is 1
    1
    """
    # Base case
    if s == []:
        return 1
    if len(s) == 1:
        return s[0]
    
    # Recrsuive case
    even_prod = s[0]
    odd_prod = s[1]
    
    if len(s) == 3:
        even_prod *= max_product(s[2:])
    elif len(s) == 4:
        even_prod *= max(max_product(s[2:]), max_product(s[3:]))
        odd_prod *= max_product(s[3:])
    else:
        even_prod *= max(max_product(s[2:]), max_product(s[3:]))
        odd_prod *= max(max_product(s[3:]), max_product(s[4:]))

    return max(even_prod, odd_prod)

# Solution
# Understood: I've went one iteration too deep
def max_product(s):
    """Return the maximum product of non-consecutive elements of s.

    >>> max_product([10, 3, 1, 9, 2])   # 10 * 9
    90
    >>> max_product([5, 10, 5, 10, 5])  # 5 * 5 * 5
    125
    >>> max_product([])                 # The product of no numbers is 1
    1
    """
    if s == []:
        return 1
    if len(s) == 1:
        return s[0]
    else:
        return max(s[0] * max_product(s[2:]), max_product(s[1:]))
        # OR
        return max(s[0] * max_product(s[2:]), s[1] * max_product(s[3:]))


# Q3
def sums(n, m):
    """Return lists that sum to n containing positive numbers up to m that
    have no adjacent repeats.

    >>> sums(5, 1)
    []
    >>> sums(5, 2)
    [[2, 1, 2]]
    >>> sums(5, 3)
    [[1, 3, 1], [2, 1, 2], [2, 3], [3, 2]]
    >>> sums(5, 5)
    [[1, 3, 1], [1, 4], [2, 1, 2], [2, 3], [3, 2], [4, 1], [5]]
    >>> sums(6, 3)
    [[1, 2, 1, 2], [1, 2, 3], [1, 3, 2], [2, 1, 2, 1], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    """
    if n < 0:
        return []
    if n == 0:
        sums_to_zero = []     # The only way to sum to zero using positives
        return [sums_to_zero] # Return a list of all the ways to sum to zero
    result = []
    for k in range(1, m + 1):
        result = result + [ [k] + rest for rest in sums(n - k, m) if rest == [] or rest[0] != k ]
    return result