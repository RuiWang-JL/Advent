with open('day.txt', 'r+') as f:
    line = f.readlines()
nums = [ord(ele) for ele in list(line[0])]


def react(nums):
    res = []
    for ele in nums:
        if len(res) > 0 and abs(res[-1] - ele) == 32:
            res.pop()
        else:
            res.append(ele)
    return len(res)


def reduce(num, nums):
    res = []
    for ele in nums:
        if num != ele and (num - 32) != ele:
            res.append(ele)
    return res


a = ord("a")
z = ord("z")
resAtoZ = []
for i in range(a, z+1):
    x = react(reduce(i, nums))
    resAtoZ.append(x)
print(min(resAtoZ))
# print("part1: {}".format(react(nums)))
