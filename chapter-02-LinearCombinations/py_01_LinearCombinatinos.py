"""
technique: always deem a vector(x, y) as the scalable result of (î, ĵ)
i.e., Vector(3, 2), means (î * 3, ĵ * -2)

! î, ĵ are the standard "basis vectors" of the xy coordinate system (two-dimensional)

so, we gonna implement this notation into our class

! "Linear combinations" of v-hat and w-hat 
"linear combinations" = a * v-hat + b * w-hat (a, b are scalars)

! the "span" of v-hat and w-hat is the SET of all their "linear combinatinos"
span = a * v-hat + b * w-hat (let a and b vary over all real numbers)

vectors vs points
when dealing with a collection of vectors, think vectors as points
otherwise, think a vector as arrow.

! "linear dependent" 
u-hat = a * v-hat + b * w-hat
for some values of a and b

! "linear independent"
w-hat != a * v-hat
for all values of a

"""

import sys
sys.path.append('.')
from libraries.vector import Vector
import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

class ScaleNotationVector(Vector):
    def __str__(self):
        return '{!r} means ({}*î, {}*ĵ)'.format(self, self.x, self.y)

v1 = ScaleNotationVector(3, -2)
v2 = ScaleNotationVector(-5, 2)
logging.debug(v1)
logging.debug(v2)