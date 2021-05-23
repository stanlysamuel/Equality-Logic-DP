# This module contains functions that will test each of the three functions bryant, dpllt and dnf-eg
from equality_logic_algorithms.bryant import bryant
from equality_logic_algorithms.dpllt import dpllt
from equality_logic_algorithms.dnf_eg import dnf_eg

from test_cases import *

# Testing Bryant: Ten test cases of the form test_formula*_bryant()
def test_formula1_bryant():
    assert bryant(formula1) == z3.unsat

def test_formula5_bryant():
    assert bryant(formula5) == z3.sat

# Testing DPLL(T): Ten test cases of the form test_formula*_dpllt()
def test_formula1_dpllt():
    assert dpllt(formula1) == z3.unsat

def test_formula5_dpllt():
    assert dpllt(formula5) == z3.sat

# Testing DNF+Equality Graph: Ten test cases of the form test_formula*_dnf_eg()
def test_formula1_dnf_eg():
    assert dnf_eg(formula1) == z3.unsat

def test_formula5_dnf_eg():
    assert dnf_eg(formula5) == z3.sat