class ReversedSequenceIterator:
    """A reversed iterator for any of Python's sequence types."""

    def __init__(self, sequence):
        """Create an iterator for the given sequence."""
        self._seq = sequence          # keep a reference to the underlying data
        self._k = len(sequence)       # will decrement to last index on first call to next

    def __next__(self):
        """Return the next element, or else raise StopIteration error."""
        self._k -= 1                    # advance to previous index
        if self._k >= 0:
            return(self._seq[self._k])  # return the data element
        else:
            raise StopIteration()       # there are no more elements

    def __iter__(self):
        """By convention, an iterator must return itself as an iterator."""
        return self


if __name__ == "__main__":
    semirp = ReversedSequenceIterator([2, 3, 5, 7, 11])
    for prime in semirp:
        print(prime)
