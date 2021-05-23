from z3 import *

x1 = Real('x1')
x2 = Real('x2')
x3 = Real('x3')

formula1 = And(x1==x2, x2==x3, x1!=x3)
formula5 = Implies(And(x1==x2, x2==x3), x1==x3)