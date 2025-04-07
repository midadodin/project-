def can_sort_containers(test_cases):
    results = []
    
    for test in test_cases:
        K, priorities = test[0], test[1]
        
        # Initialize stack and current priority
        stack = []
        sorted_priorities = sorted(priorities)
        current_priority_index = 0
        
        for priority in priorities:
            # Move items from stack to output if they match the current expected priority
            while stack and stack[-1] == sorted_priorities[current_priority_index]:
                stack.pop()
                current_priority_index += 1
            
            # If the current container matches the expected priority
            if priority == sorted_priorities[current_priority_index]:
                current_priority_index += 1
            else:
                stack.append(priority)
        
        # Final check if we can move all remaining items from the stack
        while stack and stack[-1] == sorted_priorities[current_priority_index]:
            stack.pop()
            current_priority_index += 1
        
        # If all containers are correctly sorted
        if current_priority_index == K:
            results.append(1)
        else:
            results.append(0)
    
    return results

# Reading input
import sys

data = input().split()
index = 0
N = int(data[index])
index += 1

test_cases = []
for _ in range(N):
    data = input().split()
    K = int(data[0])
    priorities = list(map(float, data[1:]))
    test_cases.append((K, priorities))

# Getting results
results = can_sort_containers(test_cases)

# Printing results
for result in results:
    print(result)
