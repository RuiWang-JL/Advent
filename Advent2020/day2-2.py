import sys, os

count = 0

class Data:
    def __init__(self, rule_times, rule_character, password):
        self.rule_times = rule_times
        self.rule_character = rule_character
        self.password = password


with open('day2.txt', 'r+') as f:
    lines=f.readlines()
    for line in lines:
        times = line.split()[0]
        low = int(times.split('-')[0])
        high = int(times.split('-')[1])
        chara = line.split()[1][0:1]
        password = line.split()[2]
        if password[low-1] is chara and password[high-1] is not chara:
            count += 1
            print(password)
        if password[low-1] is not chara and password[high-1] is chara:
            count += 1
            print(password)

print(count)