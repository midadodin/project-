def main():
    n = int(input())
    k = int(input())
    petya_row = int(input())
    petya_seat = int(input())

    petya_place = petya_row * 2 - (2 - petya_seat)
    petya_number = petya_place % k
    if petya_number == 0:
        petya_number = k

    vasya_place = -1
    if petya_place + k < n:
        vasya_place = petya_place + k
    elif petya_place - k > 0:
        vasya_place = petya_place - k
    else:
        print(vasya_place)
        return
    if vasya_place % 2 == 0:
        print(vasya_place // 2, 2)
    else:
        print(vasya_place // 2, 1)

main()