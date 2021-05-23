from z3 import *

#Function that implements DNF + Equality Graph algorithm for Equality Logic SAT
def dnf_eg(formula):
    #Dummy code. Replace your code here and your code should return z3.sat object if your claim the formula to be sat and z3.unsat otherwise
    #Eg: A valid return for this function is:
    # return z3.sat
    # DO NOT RETURN STRINGS i.e. print("sat") or return "sat" 
    s = Solver()
    return s.check(formula)