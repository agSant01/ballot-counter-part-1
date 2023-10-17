class ArrayList():
    def __init__(self, size=10) -> None:
        self.array = [None] * size
        self.size = size
        self.count = 0

    def append(self, object_):
        if self.count + 1 > self.size // 2:
            self._resize(self.size * 2)
        self.array[self.count] = object_
        self.count += 1

    def remove(self, index: int):
        if index >= self.count or index < 0:
            return None

        item_to_ret = self.array[index]

        while index < self.count:
            self.array[index] = self.array[index+1]
            index += 1
        self.count -= 1
        if self.count < self.size // 4:
            self._resize(self.size // 2)

        return item_to_ret

    def insert(self, index: int, object_):
        if self.count + 1 > self.size // 2:
            self._resize(self.size * 2)

        ptr = self.count

        while ptr > index:
            self.array[ptr] = self.array[ptr-1]
            ptr -= 1

        self.array[index] = object_
        self.count += 1

    def getElement(self, index: int):
        if index >= self.count or index < 0:
            return None
        return self.array[index]

    def _resize(self, newSize):
        newArray = [None] * newSize
        for idx, item in enumerate(self.array):
            newArray[idx] = item
        self.array.clear()
        self.array = newArray
        self.size = newSize

    def __str__(self) -> str:
        str_to_ret = []
        for i in range(self.count):
            str_to_ret.append(str(self.array[i]))
        return f'<ArrayList items: [{", ".join(str_to_ret)}]>'
