def find_max_leave_at_least_x_for_rest_from_where(l, where, x):
    if x == 0:
        nl = l[where:]
    else:
        nl = l[where: -x]
    m = max(nl)
    i = nl.index(m) + where + 1
    return m, i


def func1(filename='input.txt'):
    t = 0
    n = 12
    with open(filename) as f:
        input = [line.strip() for line in f]
    for line in input:
        l = [int(x) for x in line]
        where = 0
        for x in range(n-1, -1, -1):
            m, where = find_max_leave_at_least_x_for_rest_from_where(l, where, x)
            t += m * (10 ** (x))
    print(t)

func1('test.txt')
func1('input.txt')

