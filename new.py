import numpy as np
print(np.array([1,2,3,4]))

from packages.maths import addition
print(addition(5,6))

from packages import maths
print(maths.addition(4,5))

from packages.maths import *
print(addition(4,8))
print(substraction(9,4))

from packages.maths import *
from packages.subpackages.mult import multiplication
print(addition(3,2))
print(substraction(7,2))
print(multiplication(3,4))