"""8n log2 n < 2n^2
<=> 4 log2 n < n
Answer is 17."""

from math import log2

n = 2
a = 4 * log2(n)
while a >= n:
    n += 1
    a = 4 * log2(n)

print(n)
