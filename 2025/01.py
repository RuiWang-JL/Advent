def func1():
    with open('01.txt', 'r+') as f:
        lines = [line.strip() for line in f.readlines()]
        total = 50
        password = 0
        for line in lines:
            if line[0] == 'L':
                step = -(int(line[1:]))
            else:
                step = int(line[1:])
            total = (total + step) % 100
            if total == 0:
                password = password + 1

    print(password)


def func2():
    with open('01.txt', 'r+') as f:
        lines = [line.strip() for line in f.readlines()]
        pos = 50
        password = 0
        for line in lines:
            if line[0] == 'L':
                step = -(int(line[1:]))
                rounds = abs(step) // 100
                step = step + (rounds * 100)
            else:
                step = int(line[1:])
                rounds = step // 100
                step = step - (rounds * 100)
            password += rounds
            if pos + step >= 100 or pos + step <= 0 and pos != 0:
                password += 1

            pos = (pos + step) % 100

    print(password)

func1()
func2()