def find_marker(input, marker):
    for i in range(len(input)):
        if input[i] == marker:
            return i


def get_range(line):
    parts = line.split('-')
    return int(parts[0]), int(parts[1])


def sort_base_on_start(input):
    return sorted(input, key=lambda line: get_range(line)[0])


def func1(filename='input.txt'):
    t = 0
    with open(filename) as f:
        input = [line.strip() for line in f]
    m = find_marker(input, '')
    for line in input[m+1:]:
        veg = int(line)
        for r in range(m):
            low, high = get_range(input[r])
            if low <= veg <= high:
                t += 1
                break
    print(t)


def func2(filename='input.txt'):
    t = 0
    with open(filename) as f:
        input = [line.strip() for line in f]
    m = find_marker(input, '')
    ranges = (sort_base_on_start(input[0:m]))
    nlow, nhigh = get_range(ranges[0])
    for line in ranges:
        low, high = get_range(line)
        if low <= nhigh:
            nhigh = max(nhigh, high)
        else:
            t += nhigh - nlow + 1
            nlow, nhigh = low, high

    t += nhigh - nlow + 1
    print(t)


# func1('test.txt')
# func1('input.txt')
# func2('test.txt')
func2('input.txt')

