"""
Tuning Trouble
"""

def read_input_stream():
    with open('input_6.txt', 'r') as input_file:
        for line in input_file.readlines():
            line = line.strip()
            return line

def traverse_data(line):
    window = dict()
    my_letters = list(line)
    start = 0
    end = 13
    for i in range(end+1):
        if my_letters[i] not in window:
            window[my_letters[i]] = 1
        else:
            window[my_letters[i]] += 1

    while len(window) != 14 and end < len(my_letters):
        window[my_letters[start]] -= 1
        if window[my_letters[start]] == 0:
            del window[my_letters[start]]
        start += 1
        end += 1
        if my_letters[end] not in window:
            window[my_letters[end]] = 1
        else:
            window[my_letters[end]] += 1

    if len(window) == 14:
        return end + 1
    return -1



line = read_input_stream()
print(line)
print(traverse_data(line))
