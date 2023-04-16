def say_hello(**name):
    print('Hi {}'.format(name['Mname']))


say_hello(fname='Prince', Mname="Kofi", l_name='Asiedu')

x = lambda x, a : x + a
print(x(10, 9))