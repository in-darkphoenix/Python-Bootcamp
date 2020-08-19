def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a, b)
    else:
        return max(a, b)


def animal_crackers(w):
    sl = w.lower().split()
    return sl[0][0] == sl[1][0]


def makes_twenty(a, b):
    if a == 20 or b == 20 or a + b == 20:
        return True
    return False


def old_macdonald(w):
    f3 = w[0:3]
    s3 = w[3:]
    return f3.capitalize() + s3.capitalize()


def master_yoda(w):
    wl = w.split()
    return ' '.join(wl[::-1])


def almost_there(n):
    if n in range(90, 111):
        return True
    elif n in range(190, 211):
        return True
    else:
        return False


def almost_there2(n):
    return abs(100 - n) <= 10 or abs(200 - n) <= 10


def has33(nums):
    for i in range(0, len(nums) - 1):
        if nums[i:i + 2] == [3, 3]:
            return True
    return False


def paper_doll(w):
    r = ''
    for char in w:
        r += char * 3
    return r


def blackjack(a, b, c):
    s = a + b + c
    if s <= 21:
        return s
    elif a == 11 or b == 11 or c == 11:
        if s - 10 <= 21:
            return s - 10
    else:
        return 'Bust'


def summer_69(arr):
    s = 0
    add = True

    for n in arr:
        while add:
            if n != 6:
                s += n
                break
            else:
                add = False
        while not add:
            if n != 9:
                break
            else:
                add = True
                break
    return s


def spy_game(l):
    code = [0, 0, 7, 'x']
    for i in l:
        if i == code[0]:
            code.pop(0)
    return code[0] == 'x'


import math


def count_primes(nums):
    c = 0
    i = 2
    while i <= nums:
        d = 2
        ind = 0
        while d <= math.sqrt(i):
            if i % d == 0:
                ind = 1
                break
            d += 1
        if ind == 0:
            c += 1
        i += 1
    return c


def vol(r):
    return (4 / 3) * 3.14 * (r ** 3)


def ran_check(n, l, h):
    if n in range(l, h + 1):
        print('value in range')
    else:
        print('value not in range')


def up_low(s):
    sd = {"uc": 0, "lc": 0}
    for c in s:
        if c.isupper():
            sd["uc"] += 1
        elif c.islower():
            sd["lc"] += 1
        else:
            pass
    print('Lower case letters - ', sd["lc"])
    print('Upper case letters - ', sd["uc"])


def unique_list(l):
    x = []
    for i in l:
        if i not in x:
            x.append(i)
    return x


def multiply(l):
    ans = 1
    for i in l:
        ans *= i
    return ans


def palindrome(s):
    return s == s[::-1]


import string


def ispangram(s, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(s.lower())


print(lesser_of_two_evens(3, 5))
print(animal_crackers('Crazy cat'))
print(makes_twenty(1, 5))
print(old_macdonald('phoenix'))
print(master_yoda('I am an Assassin'))
print(almost_there(210))
print(almost_there2(89))
print(has33([1, 2, 3, 3]))
print(paper_doll('Hello'))
print(blackjack(9, 9, 9))
print(summer_69([4, 5, 6, 9, 2]))
print(spy_game([1, 0, 2, 0, 4, 0, 7]))
print(count_primes(1000))
print(vol(7))
ran_check(10, 0, 10)
up_low('Hello I am Ankit, and i am an Assassin')
print(unique_list([1, 1, 1, 2, 3, 1, 4, 4, 3, 2, 5, 5]))
print(multiply([2, 3, -4, 1]))
print(palindrome('madam'))
print(ispangram('the quick brown fox jumps over the lazy dog'))
