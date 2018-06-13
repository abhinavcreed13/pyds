#Array Implementation
class array():

    _array = None
    _size = None
    length = 0

    def __init__(self,_size):
        self._array = list()
        self._size = _size
        _idx = 0
        while _idx < self._size:
            self._array.append(None)
            _idx = _idx + 1

    #traversal
    def print(self):
        _idx = 0
        while _idx < self._size:
            print(_idx, self._array[_idx])
            _idx = _idx + 1

    #insertion
    def insert(self,index,item):
        if index < self._size:
            self._array[index] = item
            self.length = len(self._array)
        else:
            raise Exception('IndexOutOfBounds')

    #deletion
    def delete(self,index):
        if index < self._size:
            _ele = self._array[index]
            self._array[index] = None
            return _ele
        else:
            raise Exception('IndexOutOfBounds')

    #search

    #sorting

    #merging


