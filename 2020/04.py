import sys, os
import re
from collections import defaultdict


passports = []
passport = {}
count = 0
exps = {"pid", "ecl", "hcl", "hgt", "eyr", "iyr", "byr"}
exps_op = {"pid", "ecl", "hcl", "hgt", "eyr", "iyr", "byr", "cid"}

def checkPassport(passport):
    if  int(passport['byr']) >=1920 and int(passport['byr']) <= 2002 and int(passport['iyr']) >=2010 and int(passport['iyr']) <= 2020 and int(passport['eyr']) >=2020 and int(passport['eyr']) <= 2030 :
        return True 
def checkPassport2(passport):
    if re.match(r"^[0-9]{9}", passport['pid']) and len(passport['pid'])==9 and re.match(r"#[0-9a-f]{6}", passport['hcl']):
        return True
def checkPassport3(passport):
    if 'in' in passport['hgt'][-2:] and 59 <=int(passport['hgt'][:-2]) <= 76:
        return True
    elif 'cm' in passport['hgt'][-2:] and 150<=int(passport['hgt'][:-2]) <= 193:
        return True
def check(passport):
    if passport['ecl'] in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
        return True

with open('day4.txt', 'r+') as f:
    lines = f.readlines()
    for line in lines:
        newline = line.split()
        if newline:
            for element in newline:
                key, value = element.split(":")
                passport[key] = value
        else:
            if (set(passport.keys()) == exps or set(passport.keys()) == exps_op) and checkPassport(passport) and checkPassport2(passport) and checkPassport3(passport) and check(passport):
                count = count +1 
            passport.clear()
    print(count) 