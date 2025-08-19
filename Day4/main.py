# main.py
from my_package import module1
print(module1.greet("Alice"))


import math_utils

print(math_utils.add(5, 3))       # 8
print(math_utils.area_circle(2)) # 12.566...

import math_utils
print(math_utils.add(2, 3))

from math_utils import add
print(add(2, 3))

from math_utils.arithmetic import subtract
print(subtract(5, 2))

from math_utils import *
print(add(1, 1))  # Only works if __all__ is defined