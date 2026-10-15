LLIURE = "L"
OCUPAT = "O"
ESBORRAT = "B"


class MyHashMap:

    def __init__(self, cap=13):
        self._table = [[None, None, LLIURE] for _ in range(cap)]
        self._n = 0

    def _hash_function(self, key):
        return key % len(self._table)

    def _find(self, key):
        m = len(self._table)
        j = self._hash_function(key)
        for i in range(m):
            pos = (j + i) % m
            slot = self._table[pos]
            if slot[2] == LLIURE:
                return None
            if slot[2] == OCUPAT and slot[0] == key:
                return pos
        return None

    def put(self, key: int, value: int) -> None:
        m = len(self._table)
        j = self._hash_function(key)
        primera = None 
        for i in range(m):
            pos = (j + i) % m
            slot = self._table[pos]
            if slot[2] == OCUPAT:
                if slot[0] == key:
                    slot[1] = value
                    return
            elif slot[2] == ESBORRAT:
                if primera is None:
                    primera = pos
            else:
                if primera is None:
                    primera = pos
                break
        self._table[primera] = [key, value, OCUPAT]
        self._n += 1
        if self._n > len(self._table) // 2:
            self._resize(2 * len(self._table) - 1)

    def get(self, key: int) -> int:
        pos = self._find(key)
        if pos is None:
            return -1
        return self._table[pos][1]

    def remove(self, key: int) -> None:
        pos = self._find(key)
        if pos is not None:
            self._table[pos] = [None, None, ESBORRAT]
            self._n -= 1

    def _resize(self, c):
        vella = self._table
        self._table = [[None, None, LLIURE] for _ in range(c)]
        for slot in vella:
            if slot[2] == OCUPAT:
                j = self._hash_function(slot[0])
                while self._table[j][2] != LLIURE:
                    j = (j + 1) % c
                self._table[j] = [slot[0], slot[1], OCUPAT]

    def __len__(self):
        return self._n