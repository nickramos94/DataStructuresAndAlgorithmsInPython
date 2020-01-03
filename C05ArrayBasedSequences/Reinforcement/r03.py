# The results are different but asymptotically the same as in Code Fragment 5.2

import sys

data = [None] * 10000
last_size = None
while data:
    size = sys.getsizeof(data)
    if size != last_size:
        print(f"Length : {len(data):>4} | Size in bytes : {size:>5} | Byte per element : {size/len(data):.3f}")
        last_size = size
    data.pop()
