"""
implementation vector concept in python.
create a class which depict characteristics of vector concept.

! what?
vector      : length + direction
symbolic    : [a, b]
by default  : always starts from origin

calculation
addition, vector 1 + vector 2 
scalable, v1 * 2

+-----------+------------+--------------------------+---------------------------------+
| items     | Physics    | Computer Science         | Mathematcian                    |
+===========+============+==========================+=================================+
| vector    | arrow      | list of ordered numbers  | anything, addition and scalable |
+-----------+------------+--------------------------+---------------------------------+
| symbol    |   ?        |     ?                    |        ?                        |
+-----------+------------+--------------------------+---------------------------------+

in Linear algebra, vector's tail is always rooted at origin.
whenever meet a vector, always think it is in a (x, y) coordinates system.
whenever meet a vector, always think it is walking from the origin to the final point. "movement"

! why?
stfu

! how
i have no fking idea
"""

import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')
import sys
sys.path.append('.')
from libraries.vector import Vector

if __name__ == "__main__":
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    r  = v1 + v2
    logging.debug('v1      = {!r}'.format(v1))
    logging.debug('v2      = {!r}'.format(v2))
    logging.debug('v1 + v2 = {}'.format(r))
    logging.debug('v2 * 2  = {}'.format(v2 * 2))