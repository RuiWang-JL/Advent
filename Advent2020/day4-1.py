import sys, os
import re
from collections import defaultdict


passports = []
passport = {}
count = 0

def checkPassport(passport):
    if re.match(r"^[0-9]{4}", passport['byr'])  and re.match(r"^[0-9]{4}", passport['iyr']) and re.match(r"^[0-9]{4}", passport['eyr']) and int(passport['byr']) >=1920 and int(passport['byr']) <= 2002 and int(passport['iyr']) >=2010 and int(passport['iyr']) <= 2020 and int(passport['eyr']) >=2020 and int(passport['eyr']) <= 2030 :
        return True 

def checkPassport2(passport):
    if re.match(r"^[0-9]{9}", passport['pid']) and len(passport['pid'])==9 and re.match(r"#[0-9a-f]{6}", passport['hcl']):
        return True
def checkPassport3(passport):
    if 'in' in passport['hgt'][-2:] and int(passport['hgt'][:-2]) <= 76 and int(passport['hgt'][:-2]) >= 59:
        return True
    elif 'cm' in passport['hgt'][-2:] and int(passport['hgt'][:-2]) <= 193 and int(passport['hgt'][:-2]) >= 150:
        return True

def check(passport):
    if ('amb' in passport['ecl'] or 'blu' in passport['ecl']  or 'brn' in passport['ecl']  or 'gry' in passport['ecl']  or 'grn' in passport['ecl']  or 'hzl' in passport['ecl']  or 'oth' in passport['ecl'] ):
        return True

with open('day4.txt', 'r+') as f:
    
    lines = f.readlines()
    # passport['a'] = 'la'
    # passports.append(passport)
    for line in lines:
        newline = line.split()
        if len(newline)>0:
            for element in newline:
                passport[element[:3]]=(element[4:])  
        else:
            if len(passport) == 8 and checkPassport(passport) is True and checkPassport2(passport) is True and checkPassport3(passport) is True and check(passport) is True:
                count = count +1
                print(passport)
            elif len(passport) == 7:
                if 'cid' not in passport:
                    if checkPassport(passport) is True and checkPassport2(passport) is True and checkPassport3(passport) is True and check(passport) is True:
                        count = count +1   
                        print(passport)
            passport.clear()
    print(count)
    print(passports)    