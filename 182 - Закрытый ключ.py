import math

def count_pairs(x, y):
    if y % x != 0:
        return 0

    n = y // x

    divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)

    count = 0
    for p1 in divisors:
        q1 = n // p1
        if math.gcd(p1, q1) == 1:
            count += 1
    
    return count

x, y = map(int, input().split())

result = count_pairs(x, y)

print(result)
