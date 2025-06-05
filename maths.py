import math

# COUNT DIGITS - Brute Force Approach - Time Complexity: O(log10N + 1)


def countDigits(n):
    count = 0

    while n > 0:
        count = count + 1
        n = n // 10

    return count


counts = countDigits(100335467567567)
print(counts)


# COUNT DIGITS - Optimal Approach - Time Complexity: log10 N + 1
def countDigit(n):

    count = int(math.log10(n) + 1)

    return count


counts1 = countDigit(23543848857829387567839857637)
print(counts1)


# Reverse Digits of A Number
def reverseDigit(n):
    revNum = 0

    while n > 0:
        ld = n % 10
        revNum = (revNum * 10) + ld

        n = n // 10
    return revNum


reverse = reverseDigit(1234)
print(reverse)

# Check if a number is Palindrome or Not


def paliandrome(n):
    revNum = 0

    dup = n

    while (n > 0):
        ld = n % 10
        revNum = (revNum * 10) + ld

        n = n // 10

    if dup == revNum:
        return True
    else:
        return False


isPaliandrome = paliandrome(122)

print(isPaliandrome)


# Find GCD of two numbers
# Brute Force Approach - Time Complexity: O(min(N1, N2))
def find_gcd_brute(n1, n2):
    gcd = 1
    for i in range(1, min(n1, n2) + 1):
        if n1 % i == 0 and n2 % i == 0:
            gcd = i
    return gcd

# Better Approach - Time Complexity: O(min(N1, N2))


def find_gcd_better(n1, n2):
    for i in range(min(n1, n2), 0, -1):
        if n1 % i == 0 and n2 % i == 0:
            return i
    return 1


# Optimal Approach: The Euclidean Algorithm - O(min(N1, N2))
def find_gcd_optimal(n1, n2):
    while n1 > 0 and n2 > 0:
        if n1 > n2:
            n1 = n1 % n2
        else:
            n2 = n2 % n1
    if n1 == 0:
        return n2

    return n1


print(find_gcd_brute(15, 35))
print(find_gcd_better(15, 35))
print(find_gcd_optimal(15, 35))


# Armstrong Number - Time Complexity: O(log10N + 1)
def isArmstrong(num):
    k = len(str(num))
    total = 0
    n = num

    while n > 0:
        ld = n % 10
        total += ld ** k
        n = n // 10

    return total == num


print(isArmstrong(153))

# Print all Divisors of a given Number
# Brute Force Approach: Time Complexity: O(N)


def print_divisorsBrute(n):
    divisors = []
    for i in range(1, n + 1):
        if (n % i == 0):
            divisors.append(i)
    return divisors


print(print_divisorsBrute(36))


# Optimal Approach: Time Complexity: O(sqrt(N))
def print_divisorsOptimal(n):
    divisors = []
    sqrt = int(math.sqrt(n))

    for i in range(1, sqrt + 1):

        if (n % i == 0):
            divisors.append(i)

            if i != n // i:
                divisors.append(n // i)

    return divisors


print(sorted(print_divisorsOptimal(1000)))


# Check if a number is prime or not
# Brute Force Approach - Time Complexity: O(N)
def checkPrimeBrute(n):
    count = 0
    for i in range(1, n + 1):
        if (n % i == 0):
            count += 1

    if count == 2:
        return True
    else:
        return False


print(checkPrimeBrute(5))

# Optimal Approach - Time Complexity: O(sqrt(N))


def checkPrimeOptimal(n):
    count = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if (n % i == 0):
            count += 1
            if n // i != i:
                count += 1

    if count == 2:
        return True
    else:
        return False


print(checkPrimeOptimal(6))
