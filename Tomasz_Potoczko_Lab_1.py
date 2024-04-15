import time
import math
import random
import string

def zad1(arg):
    if len(arg)>1:
        return arg[0].isnumeric()
    return False

def zad2(arg):
    return arg.isnumeric()

def zad3(arg, arg1):
    x = arg1.find(arg)
    return True if x>=0 else False, (x, x+len(arg) if x>=0 else -1)

def zad4(arg, arg1):
    all_ranges = []
    x = arg1.find(arg)
    cut = 0
    
    if x<0:
        return [(-1, -1)]
    
    while True:
        print(arg1, x)
        time.sleep(0.1)
        x = arg1.find(arg)
        if x==-1:
            break
        
        all_ranges.append((x+cut, x+len(arg)))
        arg1 = arg1[x+1:]
        cut+=x+1
        if len(arg1) <= len(arg):
            break
            
        
    return all_ranges


def zad5():
    return [math.sqrt(i) for i in range(1, 257) if i%2 == 0]
        
def zad6():
    dict_24004 = {}
    for i in range(10, 21):
        dict_24004[i] = ''.join(random.choice(string.ascii_lowercase) for j in range(8))
        
    return dict_24004

#def zad7():
    #from utils.obliczenia import f1, f2, f3
    #def f1(*args): return sum(args)
    # ...
    #a = f1(args)
    #...

def zad8():
    r = ''.join(random.choice(string.ascii_lowercase) for j in range(100))
    some_dik = {}
    for i in set(r):
        some_dik[i] = r.count(i)
        
    return [list(i) for i in some_dik.items()]

def zad9():
    class Vehicle:
        def __init__(self, name, rok_produkcji, przebieg):
            self._name = name
            self._rok_produkcji = rok_produkcji
            self._przebieg = przebieg

        @property
        def name(self):
            return self._name
        
        @name.setter
        def name(self, name):
            self._name = name

        @property
        def rok_produkcji(self):
            return self._rok_produkcji
        
        @rok_produkcji.setter
        def rok_produkcji(self, rok_produkcji):
            self._rok_produkcji = rok_produkcji

        @property
        def przebieg(self):
            return self._przebieg
        
        @przebieg.setter
        def name(self, przebieg):
            self._przebieg = przebieg
        
        def is_old(self):
            return self._rok_produkcji<1970
        def is_long_milage(self):
            return self._przebieg>100_000
            
    class Car(Vehicle):
        def __init__(self, name, rok_produkcji, przebieg):
            super().__init__(name, rok_produkcji, przebieg)
    
    v = Vehicle('SupaNiga', 1245, 130_000)
    c = Car('SupaCar', 1998, 30_000)

    print('Vehicle: old, milage: (', v.is_old(), v.is_long_milage())
    print('Car: old, milage: (', c.is_old(), c.is_long_milage())

def zad10():
    alphabet = [chr(i) for i in range(97, 123)]
    with open('alphabet1-24004.txt', 'w') as f:
        f.write(''.join(alphabet))
        
    with open('alphabet2-24004.txt', 'w') as f:
        for c in alphabet:
            f.write(c+'\n')
    
if __name__ == '__main__':
    zad9()

    
