
class Stack:

    def __init__(self, ls=None):
        if ls is None:
            ls = []
        self.ls = ls

    def is_empty(self):
        if len(self.ls) == 0:
            return True
        else:
            return False

    def push(self, item):
        self.ls.append(item)

    def pop(self):
        return self.ls.pop(-1)

    def peek(self):
        return self.ls[-1]

    def size(self):
        return len(self.ls)
