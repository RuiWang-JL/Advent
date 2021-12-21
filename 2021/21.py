from collections import defaultdict
import copy
import time
start_time = time.time()


start1 = 4
start2 = 8


def play(start1, start2):
    die = 0
    socre2, socre1 = 0, 0
    pos1, pos2 = start1, start2
    player1 = True
    while True:
        if socre1 >= 1000 or socre2 >= 1000:
            print("s1", socre1, "s2", socre2, "die", die)
            print(die*min(socre1, socre2))
            return socre1, socre2
            break
        elif die % 2 == 0:
            # die 1,2,3.....97,98,99,100,1
            d = die % 100+1
            d1 = (die+1) % 100+1
            d2 = (die+2) % 100+1
            socre = (pos1+d+d1+d2-1) % 10+1
            pos1 = socre
            socre1 += socre
            die += 3
        else:
            d = die % 100+1
            d1 = (die+1) % 100+1
            d2 = (die+2) % 100+1
            socre = (pos2+d+d1+d2-1) % 10+1
            socre2 += socre
            pos2 = socre
            die += 3


def play2(start1, start2):
    roll = defaultdict(int)
    result = defaultdict(int)
    result2 = defaultdict(int)
    score1, score2 = 0, 0
    for i in [1, 2, 3]:
        for k in [1, 2, 3]:
            for n in [1, 2, 3]:
                s = i+k+n
                roll[s] += 1
    result[start1, score1] += 1
    result2[start1, score1, start2, score2] += 1
    round = 0
    pos1, pos2 = start1, start2
    win1, win2 = 0, 0
    for round in range(0, 18):
        newresult = defaultdict(int)
        if round % 2 == 0:
            for (startpos, prescore, pos2, sc2), fstartpos in result2.items():
                for rollresult, froll in roll.items():
                    endpos = (startpos+rollresult-1) % 10+1
                    newscore = prescore + endpos
                    if newscore >= 21:
                        win1 += froll*fstartpos
                    else:
                        newresult[endpos, newscore,
                                  pos2, sc2] += froll*fstartpos
            result2 = copy.deepcopy(newresult)
        else:
            for (pos1, sc1, startpos, prescore), fstartpos in result2.items():
                for rollresult, froll in roll.items():
                    endpos = (startpos+rollresult-1) % 10+1
                    newscore = prescore + endpos
                    if newscore >= 21:
                        win2 += froll*fstartpos
                    else:
                        newresult[pos1, sc1, endpos,
                                  newscore] += froll*fstartpos
            result2 = copy.deepcopy(newresult)

        print(len(result2))
    print(win1, win2)


# play2(4, 8)
play2(7, 3)
print("--- %s seconds ---" % (time.time() - start_time))
