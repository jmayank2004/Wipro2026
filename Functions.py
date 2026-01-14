def add(a,b):
    print((a+b,a))
add(43,79)
def subtract (a,b):
    return a-b,a
print(subtract(158,122))


def hello(greeting='Hello', name='world'):
    print('%s, %s!' % (greeting, name))
hello('Greetings')


def hello_1(greeting, name):
    print('%s, %s!' % (greeting, name))
hello_1(name='world', greeting='Hello')


def print_params(*params):
    print(params)
print_params('Testing')
print_params(1, 2, 3)


def print_params_3(**params):
    print(params)
print_params_3(x=1, y=2, z=3)
