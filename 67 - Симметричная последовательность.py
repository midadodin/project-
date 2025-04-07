def is_palindrome(seq):
    return seq == seq[::-1]

def min_addition_to_palindrome(seq):
    n = len(seq)
    
    for i in range(n):
        if is_palindrome(seq[i:]):
            addition = seq[:i][::-1]
            return len(addition), addition
    
    return 0, []

N = int(input())
sequence = list(map(int, input().split()))

min_add_count, addition = min_addition_to_palindrome(sequence)

print(min_add_count)
if min_add_count > 0:
    print(" ".join(map(str, addition)))