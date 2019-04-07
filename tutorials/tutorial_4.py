# PYTHON TUTORIALS 4

### IF Statements
# x = int(input("Please enter an integer: ")) #Input Command
#
# if x < 0:
#     print("x (",x,") is less than zero")
# elif x == 0:
#     print("x (",x,") is equal to zero")
# elif x > 0:
#     print("x (",x,") is greater than zero")

### FOR Statements
# Measure some STRINGS
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w,'has',len(w),'letters.')

# Modify String within Loop
for w in words[:]:
    if len(w) > 6:
        words.insert(0,w)
print(words)

### range() Function
for i in range(6): # generates arithmetic range with # elements (0 to #-1)
    print(i)

#Set Range start/stop
range(5,10) #Creates Object of 5,6,7,8,9
range(0,10,3) #Creates object of 0,3,6,9
range(-10,-100,-30) #Creates object of-10,-40,-70

#iterate over indecies of sequence
a = ['Mary','had','a','litle','lamb']
for i in range(len(a)):
    print(i,a[i])

#List Function
list(range(len(a))) #creates list of range

# Break and Continue Statements + Else Clauses on Loops
for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print(n,'equals',x,'*',n//x)
            break
    else:
        # Loop fell through without finding a factor
        print(n,'is a prime number')

# Continue Statements
for num in range(2,10):
    if num % 2 == 1:
        print("Found an odd number", num)
        continue
    print("Found a number", num)

# Pass Statements
while False:
    pass # busy wait for keyboard interrupt (Ctrl + C)

class MyEmptyClass: #Creation of a minimal class
    pass

def initlog(*args):
    pass #REMEMBER TO IMPLEMENT THIS (Pass as Placeholder)


#Defining Functions
def fib(n): #Write Fibonaci Series up to # NOTE:
    """Print a Fibonnachi series up to n."""
    a,b = 0,1
    while a < n:
        print(a,end=' ')
        a,b = b, a+b
    print()

if __name__ == "__main__":
    fib(2000)
    f = fib
    f(100)

def fib2(n): # return Fibonnachi series up to n
    """Return a list containing Fibonacci Series"""
    result = [] #initialize Result
    a,b = 0,1 #initialize a,b
    while a<n:
        result.append(a) #see below
        a,b = b,a+b
    return result

if __name__ == "__main__":
    fib2(2000)
    f2 = fib2
    f2(100)


def ask_ok(prompt,retries=4,reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

i = 71
def f(arg = i):
    print(arg)

i = 41
f() #will print 71 since i=71 before f() is defined


def f(a, L=[]): #
    """Function that adds to L each call"""
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

def f(a, L=None):
    """Function that re-Initializes L upon Call"""
    if L is None:
        L = []
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    """Voltage is required, all others are optional. Must have keywork"""
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


"""FORMAL ARGUMENTS AND KEYWORD ARGUMENTS"""
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")


# Arbitrary Argument Lists
def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))

def concat(*args, sep="/"):
    return sep.join(args)

print(concat("earth","mars","venus"))
print(concat("earth","mars","venus",sep=":"))


# Unpacking Argument Lists
print(list(range(3,6)))
randomsize = [3,6]
print(list(range(*randomsize)))

#Dictionary
"""DICTIONARY"""
d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)


# Lambda Expressions
def make_incrementor(n):
    return lambda x: x + n
"""Define n = 42 --> x = 42 for all make_incrementor calls """
f = make_incrementor(42)

# Lambda Expressions to Pass Small Functions within Functions
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
print(pairs)
""" Sort alphabetically by second element in each pair """
pairs.sort(key = lambda pair: pair[1])
print(pairs)


# Print Comment in Function __doc__
print(parrot.__doc__)
