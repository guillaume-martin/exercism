from collections import Counter

def score_number(dice, num):
    cnt = Counter(dice)
    try:
        score = cnt[num] * num
    except:
        score = 0

    return score

# Score categories
# Change the values as you see fit
YACHT = (lambda x: 50 if len(set(x)) == 1 else 0)
ONES =  (lambda x: score_number(x, 1))
TWOS = (lambda x: score_number(x, 2))
THREES = (lambda x: score_number(x, 3)) 
FOURS = (lambda x: score_number(x, 4))
FIVES = (lambda x: score_number(x, 5))
SIXES = (lambda x: score_number(x, 6))
FULL_HOUSE = (lambda x: sum(x) if set(Counter(x).values()) == {2,3} else 0)
FOUR_OF_A_KIND = (lambda x: Counter(x).most_common(1)[0][0] * 4 if
                  Counter(x).most_common(1)[0][1] >= 4 else 0) 
LITTLE_STRAIGHT = (lambda x: 30 if Counter(x) == Counter([1,2,3,4,5]) else 0)
BIG_STRAIGHT = (lambda x: 30 if Counter(x) == Counter([2,3,4,5,6]) else 0)
CHOICE = (lambda x: sum(x))


def score(dice, category):

    return category(dice)
