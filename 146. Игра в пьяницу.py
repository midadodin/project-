from collections import deque

def main():
    first = list(map(int, input().split()))
    second = list(map(int, input().split()))

    first = deque(first)
    second = deque(second)
    counter = 0
    stop_count = 10**6 + 1

    while first and second:
        counter += 1

        if counter == stop_count:
            print('botva')
            return
        p1_card = first.popleft()
        p2_card = second.popleft()

        if abs(p1_card - p2_card) == 9:
            print('!!!')
            if p1_card == 9:
                second.append(p1_card)
                second.append(p2_card)
            else:
                first.append(p1_card)
                first.append(p2_card)
        elif p1_card > p2_card:
            first.append(p1_card)
            first.append(p2_card)
        else:
            second.append(p1_card)
            second.append(p2_card)

    print('first', counter) if not second else print('second', counter)
    

main()