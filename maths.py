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
