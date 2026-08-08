class MyClass:
    def __init__(self):
        self._internal_value = 0  #  Convention: _ means "private"

    def get_value(self):
        return self._internal_value

obj = MyClass()
# print(obj._internal_value)  # This *works*, but it's against convention
print(obj.get_value())       # This is the preferred way