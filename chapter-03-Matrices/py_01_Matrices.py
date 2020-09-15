"""
"unfortunately, no one can be told what the Matrix is.
You have to see it for yourself."
-- Morpheus

! "linear transformation"
Vector(5, 7) -> function -> new Vector(2, 3)    "movement", "linear"

so it means,
- all lines remain lines, w/o getting curved
- the origin remains fixed in place.

BUT, how? 

! "2 * 2 Matrix"

[(a, c), (b, d)] [x, y] = x * [(a, c)] + y * [(b, d)] = [(ax + by, cx + dy)]

aha,
(î, ĵ) -> [(a, c), (b, d)]
(1, 0) î -> (a, c) # <~ new î
(0, 1) ĵ -> (b, d) # <~ new ĵ

everytime, u see a Matrix, u interpret it as a certain transformation of space.

"""
