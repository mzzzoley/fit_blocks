class Piece:

    def __init__(self, shape:list[list]):
        self.base = shape
        self.size = sum(map(sum, zip(*shape)))
        self.shape_list = [self.base]
        self.__create_possibilities()
        self.counter = 0

    def __self__(self):
        return self.shape_list

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < len(self.shape_list):
            result = self.shape_list[self.counter]
            self.counter += 1
            return result
        self.counter = 0
        raise StopIteration

    def __str__(self):
        text = ''
        for shape in self.shape_list:
            text += '\n'.join(str(r) for r in shape) + '\n' + '\n'
        return text[:-2] if text else ''

    def __is_new(self, shape:list[list]) -> bool:
        for old_shape in self.shape_list:
            if shape == old_shape:
                return False
        return True

    @staticmethod
    def __rotate(shape:list[list]):
        return [list(ls) for ls in zip(*reversed(shape))]

    @staticmethod
    def __mirror(shape:list[list]):
        return [list(ls[::-1]) for ls in shape]

    def __create_possibilities(self):
        latest = self.base
        for i in range(3):
            rotated_new = self.__rotate(latest)
            if self.__is_new(rotated_new):
                self.shape_list += [rotated_new]
                latest = rotated_new
            else:
                break

        mirrored_shape_list = []
        for shape in self.shape_list:
            mirrored_new = self.__mirror(shape)
            if self.__is_new(mirrored_new):
                mirrored_shape_list += [mirrored_new]
        if mirrored_shape_list:
            self.shape_list += mirrored_shape_list
