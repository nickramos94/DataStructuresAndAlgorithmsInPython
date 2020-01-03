# The results are different but asymptotically the same as in Code Fragment 5.2

import sys

data = []
last_size = None
for k in range(10000):
    data.append(None)
    size = sys.getsizeof(data)
    if size != last_size:
        print(f"Length : {len(data):>4} | Size in bytes : {size:>5} | Byte per element : {size/len(data):.3f}")
        last_size = size
