# comment different level of variable to see result
x = 'global'


def greet():
    # x = 'enclosed'
    def hello():
        # x = 'local'
        print('hello ' + x)

    hello()


greet()

a = 'value'


def func(a):
    print(f'a is {a}')
    a = 'new value'
    print(f'i changed the value of a locally to {a}')


func(a)
print(a)

b = 'value'


def func2():
    global b
    print(f'b is {b}')
    b = 'new value'
    print(f'i changed the value of global var. a to {b}')


func2()
print(b)
