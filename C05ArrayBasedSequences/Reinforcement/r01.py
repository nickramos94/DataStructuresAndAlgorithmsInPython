# The results are different but asymptotically the same as in Code Fragment 5.2

import sys

data = []
for k in range(100):
    print(f"Length : {len(data):03} | Size in bytes : {sys.getsizeof(data):03}")
    data.append(None)
