# Equality-Logic-DP
This repository contains the code for various decision procedures to solve the quantifier free fragment of first order logic with the theory of equality.

# Note to students

- This folder demonstrates a standard software engineering practice to develop and test Python applications. We will use pytest to professionally (and conveniently) run tests.
- Please use the exact same folder structure as used in this repository.
- The package **equality_logic_algorithms** has three modules bryant.py, dnf_eg.py and dpllt.py which denote the three algorithms you need to implement. You need to replace your code in the functions in those modules. Please do not change the names of these functions as the test functions use these names. As of now, the 3 functions just use the z3 solver to solve the formula. You need to replace your code there. If your code calls other functions apart from the ones given in the repo, they can be named anything.
- These functions are allowed to only return z3.sat or z3.unsat objects because the test functions compare against them. Thus if your formula is SAT, DO NOT print "SAT" or return "SAT". Please return the corresponding z3 objects as either:
```
return z3.sat
```
or 
```
return z3.unsat
```
There is no need to return the model. If you have done that, well and good but as discussed in the tutorial, we will not consider it.
- The folder **tests** contain two files. 
    - *test_cases.py* should contain the ten test cases that Habeeb gave named formula*.py. For now, formula1 and formula5 is given. Please fill the rest.
    - *test_functions.py* include the tests for each formula-algorithm combination. Thus there will be 10\*3 = 30 test functions. For representation 2\*3 = 6 test_functions are given. Please fill the rest.
    - To run the tests, simply type
    ```
    pytest
    ```
    or
    ```
    python -m pytest
    ```
    or
    ```
    python3 -m pytest
    ```
    and you will get the following output:
    ```
    platform darwin -- Python 3.9.2, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
    rootdir: /Users/stanly/Project/Equality-Logic-DP collected 6 items                                             tests/test_functions.py ......                                                              [100%]
    ======================================== 6 passed in0.34s ========================================
    ```
