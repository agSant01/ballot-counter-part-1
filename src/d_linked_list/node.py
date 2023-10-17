class Node:
    def __init__(self, value=None, next=None, prev=None) -> None:
        self.value = value
        self.next = next
        self.prev = prev

    def clear(self):
        self.value = None
        self.prev = None
        self.next = None

    def __str__(self) -> str:
        return f'<Node value: {self.value}>'
