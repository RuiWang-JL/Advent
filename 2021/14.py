from collections import defaultdict


with open('day14.txt', 'r+') as f:
    lines = [line.strip() for line in f.readlines()]
input = lines[0]
ins = lines[2:]
k = {}
freq = defaultdict(int)
for i in ins:
    a, b = i.split("->")
    pair = a[:2]
    bet = b[1]
    k[pair] = bet
for i, ele in enumerate(input):
    pair = ""
    if i < len(input) - 1:
        pair = input[i] + input[i+1]
        freq[pair] += 1
steps = 40
for step in range(1, steps+1):
    newfreq = defaultdict(int)
    for ele, v in freq.items():
        between = k[ele]
        new1 = ele[0] + between
        new2 = between+ele[1]
        newfreq[new1] += v
        newfreq[new2] += v
    freq = newfreq
letters = defaultdict(int)
for ele, v in freq.items():
    first = ele[0]
    second = ele[1]
    letters[first] += v
letters[input[-1]] += 1

print(max(letters.values())-min(letters.values()))
