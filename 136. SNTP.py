def calculate_seconds(time):
    return 3600 * time[0] + 60 * time[1] + time[2]

def convert_time(seconds):
    daytime = 24 * 3600
    seconds %= daytime
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return f'{hours:02}:{minutes:02}:{seconds:02}'

def main():
    a = list(map(int, input().split(sep=':')))
    b = list(map(int, input().split(sep=':')))
    c = list(map(int, input().split(sep=':')))

    a_seconds = calculate_seconds(a)
    b_seconds = calculate_seconds(b)
    c_seconds = calculate_seconds(c)

    daytime = 24 * 3600

    if c_seconds < a_seconds:
        c_seconds += daytime
    delta = round((c_seconds - a_seconds) / 2)
    result = convert_time(b_seconds + delta)

    print(result)

main()