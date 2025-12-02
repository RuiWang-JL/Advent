def func1(filename='input.txt'):
    total = 0
    with open(filename) as f:
        input_line = [line.strip() for line in f][0]

    input = input_line.split(',')
    for pair in input:
        pairs = pair.split('-')
        start = pairs[0]
        end = pairs[1]
        l_s = len(start)//2
        start_1 = start[0:l_s]
        start_2 = start[l_s:]
        l_e = len(end)//2
        end_1 = end[0:l_e]
        end_2 = end[l_e:]
        # even
        if len(start) % 2 ==0:
            if int(start_1) < int(start_2):
                s = int(start_1)+1
            else:
                s = int(start_1)
        # odd
        else:
            s = 10**l_s

        if len(end) % 2 ==0:
            if int(end_1) > int(end_2):
                e = int(end_1) - 1
            else:
                e = int(end_1)
        else:
            e = 10**l_e -1
        for n in range(s, e+1):
            total += int(str(n)*2)
    print(total) # 31000881061

def func2(filename='input.txt'):
    t = set()
    with open(filename) as f:
        input_line = [line.strip() for line in f][0]
    input = input_line.split(',')
    for pair in input:
        pairs = pair.split('-')
        start = pairs[0]
        end = pairs[1]
        l_e = len(end)//2
        for n in range(1, 10**(l_e+1)):
            for repeats in range(2, len(end)+1):
                n_full = str(n)*repeats
                if int(n_full) >= int(start) and int(n_full) <= int(end):
                    t.add(int(n_full))
                    break
    print(sum(t))

func2()