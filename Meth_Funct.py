print('Welcome to the method and functions operation')


def hey_world():
    print('Hey')


def hello_world(name):
    return 'Hello ' + name


s = 'i love my cat'


def cat_check(s):
    if 'cat' in s:
        return True
    else:
        return False


def cat_check_n(s):
    return 'cat' in s.lower()


def pig_latin(w):
    """
    Description - returns the word as piglatin
    Input - string...
    Output - string...
    """
    if w[0] in 'aeiou':
        return w + 'ay'
    else:
        return w[1:] + w[0] + 'ay'


def f1(*args):
    print(sum(args))


def f2(**kwargs):
    if 'fruit' in kwargs:
        print('my favorite fruit is {}'.format(kwargs['fruit']))
    else:
        print('Nothing here')


def f3(*args, **kwargs):
    print('i will have {} {}'.format(args[1], kwargs['food']))


hey_world()
print(hello_world('Ankit'))
print(cat_check('cat'))
print(cat_check('Cat'))
print(cat_check_n('Cat'))
print(pig_latin('word'))
print(pig_latin('apple'))
help(pig_latin)
f1(1, 2, 5, 4, 3)
f2(fruit='mango', veges='bittergourd')
f2(veges='tomato')
f3(10, 20, 30, food='pizza', game='ac2')
