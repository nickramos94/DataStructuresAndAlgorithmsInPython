import ctypes


class DynamicArray:
    """A dynamic array class akin to a simplified Python list."""

    def __init__(self):
        """Create an empty array."""
        self.__len = 0                                    # count actual elements
        self.__capacity = 1                             # default array capacity
        self.__arr = self.__make_array(self.__capacity)     # low-level array

    def __len__(self):
        """Return number of elements stored in the array."""
        return self.__len

    def __getitem__(self, k):
        """Return element at index k."""
        if not -self.__len <= k < self.__len:
            raise IndexError('invalid index')
        return self.__arr[k % self.__len]                              # retrieve from array

    def append(self, obj):
        """Add object to end of the array."""
        if self.__len == self.__capacity:                  # not enough room
            self.__resize(2 * self.__capacity)             # so double capacity
        self.__arr[self.__len] = obj
        self.__len += 1

    def __resize(self, c):                            # nonpublic utitity
        """Resize internal array to capacity c."""
        new = self.__make_array(c)                        # new (bigger) array
        for k in range(self.__len):                       # for each existing value
            new[k] = self.__arr[k]
        self.__arr = new                                   # use the bigger array
        self.__capacity = c

    def __make_array(self, c):                        # nonpublic utitity
        """Return new array with capacity c."""
        return (c * ctypes.py_object)()               # see ctypes documentation

    def insert(self, k, value):
        """Insert value at index k, shifting subsequent values rightward."""
        # (for simplicity, we assume 0 <= k <= n in this verion)
        if self.__len == self.__capacity:  # not enough room
            new = self.__make_array(2 * self.__capacity)  # double capacity
            # Before k
            for i in range(k):
                new[i] = self.__arr[i]
            # k
            new[k] = value
            # After k
            for i in range(k + 1, self.__len + 1):
                new[i] = self.__arr[i - 1]
            # Replace relevant values
            self.__arr = new
            self.__capacity *= 2
        else:  # enough room
            for i in range(self.__len, k, -1):                # shift rightmost first
                self.__arr[i] = self.__arr[i - 1]
            self.__arr[k] = value                             # store newest element
        self.__len += 1

    def remove(self, value):
        """Remove first occurrence of value (or raise ValueError)."""
        # note: we do not consider shrinking the dynamic array in this version
        for k in range(self.__len):
            if self.__arr[k] == value:              # found a match!
                for j in range(k, self.__len - 1):    # shift others to fill gap
                    self.__arr[j] = self.__arr[j + 1]
                self.__arr[self.__len - 1] = None        # help garbage collection
                self.__len -= 1                       # we have one less item
                return                             # exit immediately
        raise ValueError('value not found')    # only reached if no match

    def __repr__(self):
        return f"DynamicArray([{', '.join(str(self[i]) for i in range(self.__len))}])"


if __name__ == "__main__":
    # __init__
    l = DynamicArray()
    # append
    for i in range(10):
        l.append(i)
    # __getitem__
    print(l[2])
    print(l[-2])
    print(l)
    # insert
    for i in range(10):
        l.insert(3, i)
    print(l)
