# SQURE PATTERN
def square_pattern(n):
    for i in range(n):
        print("* " * n)


square_pattern(5)

# RIGHT-ANGLED TRIANGLE PATTERN


def rightTriangle_pattern(n):
    for i in range(1, n + 1):
        print("* " * i)


rightTriangle_pattern(5)


# Right-Angled Number Pyramid Pattern prints- j
def rightTrinagleNumber_pattern(n):
    for i in range(1, n + 1):
        row = " ".join(str(j) for j in range(1, i+1))
        print(row)


rightTrinagleNumber_pattern(5)


# Right-Angled Number Pyramid Pattern prints- i
def rightTiangleSameNumber_pattern(n):
    for i in range(1, n + 1):
        print((str(i) + " ") * i)


rightTiangleSameNumber_pattern(5)

# INVERTED RIGHT STAR PYRAMID


def invertedRightStarPyramid_pattern(n):
    for i in range(n, 0, -1):
        print("* " * i)


invertedRightStarPyramid_pattern(5)


# INVERTED RIGHT NUMBER PYRAMID
def invertedRightNumberPyramid(n):
    for i in range(n, 0, -1):
        row = " ".join(str(j) for j in range(1, i+1))
        print(row)


invertedRightNumberPyramid(5)

# STAR PYRAMID


def starPyramid_pattern(n):
    for i in range(n):
        spaces = " " * (n - i - 1)
        stars = "*" * (2 * i + 1)

        print(spaces + stars)


starPyramid_pattern(5)

# INVERTED STAR PYRAMIND


def invertedStarPyramid_pattern(n):
    for i in range(n):
        spaces = " " * i
        stars = "*" * (2 * (n - i) - 1)

        print(spaces + stars)


invertedStarPyramid_pattern(5)

# DIAMOND STAR PATTERN


def diamond_star_pattern(n):
    # Upper part
    for i in range(n):
        spaces = " " * (n - i - 1)
        stars = "*" * (2 * i + 1)
        print(spaces + stars)
    # Lower part
    for i in range(n - 1):
        spaces = " " * (i + 1)
        stars = "*" * (2 * (n - i - 2) + 1)
        print(spaces + stars)


diamond_star_pattern(10)
