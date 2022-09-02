C++ dependencies:

* A recent version of the g++ compiler
* The Boost C++ library; download here: https://www.boost.org/users/history/version_1_79_0.html (put the folder into usr/gcc/include/)



Last command that worked:
cd pycom
pycom -r -o ../pycom_output_folder ../pycom_tests.py


Supported Features

    All 'turing complete' features of Python: if, else, for, while, etc.
    f'' strings
    Some in built functions
    Some math library functions
    List comprehensions
    Python-style arbitarily large intergers

Not supported yet

    Pythonic ways of writing certain blocks (one line if...else, etc.)
    Multi-line string literals
    A lot of libraries included in stdlib
    Classes
    The throw and finally keywords
    Heterogeneous lists; lists with more than one data type in them