import sys, os

samll_nums = []
new_nums_needed = []

with open('day1.txt', 'r+') as f:
    lines = f.readlines()
    for i in range(0, len(lines)):
        lines[i] = int(lines[i])
    for line in lines:
        if line < 1010:
            samll_nums.append(line)
    print(samll_nums)

    # Look in the small list
    for i in range(0, len(samll_nums)-2):
        for j in range(i+1, len(samll_nums)-1):
            for k in range(j+1,len(samll_nums)):
                sum=samll_nums[i] + samll_nums[j] + samll_nums[k]
                if sum == 2020:
                    print(samll_nums[i]*samll_nums[j]*samll_nums[k])

