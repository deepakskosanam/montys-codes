# PYTHON TUTORIALS 3

# this is the first comment
spam = 1    # and this is the second comment
            # ... and now a third!
text = "# This is not a comment because it's inside quotes."


# Numbers
a = 2 + 2
b = 50 - 5*6
c = (50- 5*6) / 4

8 / 5
2**2
13//4

# Strings
print("ba" + "na"*3)
print("clo" "se")

s = "goat"
t = s[1:]+"s"

#  Indexing for STRINGS
#  +---+---+---+---+---+---+
#  | P | y | t | h | o | n |
#  +---+---+---+---+---+---+
#  0   1   2   3   4   5   6
# -6  -5  -4  -3  -2  -1


print(len(s))

# Lists
squares = [1,4,9,16,25]
squares[-1] #[25]
squares[-3:] #[9,16,25]
squares[-3:]+squares[0:2] #[9,16,25,1,4]
squares = squares + [36] #[1,4,9,16,25,36]
squares.append(49) #[1,4,9,16,25,36,49]
squares[5:] = [] #[1,4,9,16,25]

letters = ['a','b','c']
concat = [squares,letters] # [[1,4,9,16,25],['a','b','c']]

# Fibonacci Series
print("Fibonacci Test")
a = [0,1]
while a[-1]<100:
    a.append(a[-1]+a[-2])
    print('Last Elem of a =',a[-1])
a = a[0:-1]

print(a)

print("Completed")
