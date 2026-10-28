# Q1
def swipe(n):
    """Print the digits of n, one per line, first backward then forward.

    >>> swipe(2837)
    7
    3
    8
    2
    8
    3
    7
    """
    if n < 10:
        print(n)
    else:
        print(n % 10)
        swipe(n // 10)
        print(n % 10)

# Q2
def skip_factorial(n):
    """Return the product of positive integers n * (n - 2) * (n - 4) * ...

    >>> skip_factorial(5) # 5 * 3 * 1
    15
    >>> skip_factorial(8) # 8 * 6 * 4 * 2
    384
    """
    if n < 1:
        return 1
    else:
        return n * skip_factorial(n - 2)

#Q3
def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    def is_a_factor(x):
        """Recursively checks if x is a factor, then x-1, then x-2, ... all the way until 1 unless a factor is found."""
        if x == 1:
            return True
        elif n % x == 0:
            return False
        else:
            return is_a_factor(x-1)
    sqrt = int(n**0.5)
    return is_a_factor(sqrt)

# Q4
def hailstone(n):
    """Print out the hailstone sequence starting at n, 
    and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    print(n)
    if n % 2 == 0:
        return even(n)
    else:
        return odd(n)

# If n is even, divide by 2
def even(n):
    # Calling hailstone prints and continues sequence, +1 adds a step 
    return hailstone(n//2) + 1

# If n is odd, multiply by 3 and add 1
def odd(n):
    # Base case: End of hailstone sequence
    if n == 1:
        return 1
    else:
        return hailstone(3*n+1) + 1


# Q5
def sevens(n, k):
    """Return the (clockwise) position of who says n among k players.

    >>> sevens(2, 5)
    2
    >>> sevens(6, 5)
    1
    >>> sevens(7, 5)
    2
    >>> sevens(8, 5)
    1
    >>> sevens(9, 5)
    5
    >>> sevens(18, 5)
    2
    """
    def f(i, who, direction):
        if i == n:
            return who

        # If has seven or diviisble by seven, change direction
        elif has_seven(i) or i % 7 == 0:
            direction = -direction
        # New player by adding or subtracting depending on direction
        new_who = (who + direction) % k
        # If have subtracted before player 1, loop back to player k (has to be better way to do this)
        if new_who == 0:
            new_who = k
        return f(i + 1, new_who, direction)

    return f(1, 1, 1)

# Return true if number contains a 7
def has_seven(n):
    if n == 0:
        return False
    elif n % 10 == 7:
        return True
    else:
        return has_seven(n // 10)

# Q6 - not available 