import copy


class Prototype:
    def __init__(self, value):
        self.value = value

    def clone(self):
        return copy.deepcopy(self)


original = Prototype([1, 2, 3])
cloned = original.clone()

print(original.value == cloned.value)  # True
print(original is cloned)  # False
