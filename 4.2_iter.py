class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __iter__(self):
        return iter(self._children)

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def __add__(self, node):
        self._children.append(node)

    def add_child(self, node):
        self._children.append(node)


if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root + child1
    root + child2
    for ch in root:
        print(ch)
    # Выводит Node(1), Node(2)
