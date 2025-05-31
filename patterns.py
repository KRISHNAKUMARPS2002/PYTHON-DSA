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
