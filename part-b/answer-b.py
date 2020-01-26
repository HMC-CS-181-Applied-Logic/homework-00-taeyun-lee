from propositional_logic import *

A = BoolVar('A')
B = BoolVar('B')
C = BoolVar('C')

# write code using A, B, and C, along with 
# the classes from propositional_logic.py
# and the .format() mathod to output the
# following expression:

# (((A => B) & (B => C)) => (A => C))
f1 = Implies(A, B)
f2 = Implies(B, C)
f3 = And(f1, f2)
f4 = Implies(A, C)
f5 = Implies(f3, f4)
print(f5.format())