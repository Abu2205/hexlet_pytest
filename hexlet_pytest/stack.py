class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            raise IndexError("Попытка извлечь элемент из пустого стека")
        return self.items.pop()

    def is_empty(self):
        return not self.items

