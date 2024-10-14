class ArrayStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * self.capacity
        self.top = -1

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.capacity - 1

    def push(self, item):
        if self.isFull():
            raise OverflowError("Stack is full")
        self.top += 1
        self.array[self.top] = item

    def pop(self):
        if self.isEmpty():
            raise IndexError("Stack is empty")
        item = self.array[self.top]
        self.top -= 1
        return item

    def peek(self):
        if self.isEmpty():
            raise IndexError("Stack is empty")
        return self.array[self.top]

    def __str__(self):
        return str(self.array[0:self.top + 1][::-1])

    def size(self):
        return self.top + 1


def isValidPos(x, y, maze):
    if x < 0 or y < 0 or x >= len(maze[0]) or y >= len(maze):
        return False
    return maze[y][x] == '0' or maze[y][x] == 'x'


def DFS(maze):
    print('DFS:')
    stack = ArrayStack(100)
    stack.push((0, 1))
    distance = 0

    while not stack.isEmpty():
        here = stack.pop()
        print(here, end='->')
        (x, y) = here
        distance += 1

        if maze[y][x] == 'x':
            print(f'\n출구를 찾았습니다! 이동거리 = {distance}')
            return True
        else:
            maze[y][x] = '.'
            if isValidPos(x, y - 1, maze):
                stack.push((x, y - 1))
            if isValidPos(x, y + 1, maze):
                stack.push((x, y + 1))
            if isValidPos(x - 1, y, maze):
                stack.push((x - 1, y))
            if isValidPos(x + 1, y, maze):
                stack.push((x + 1, y))
        print('현재 스택:', stack)

    print('출구를 찾지 못했습니다.')
    return False


if __name__ == "__main__":
    maze = [
        ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
        ['e', '0', '0', '0', '1', '0', '0', '0', '0', '1'],
        ['1', '0', '1', '0', '1', '0', '1', '1', '0', '1'],
        ['1', '1', '1', '0', '1', '0', '0', '0', '0', '1'],
        ['1', '0', '0', '0', '0', '1', '1', '1', '0', '1'],
        ['1', '0', '1', '1', '0', '1', '0', '0', '0', '1'],
        ['1', '0', '0', '1', '0', '0', '0', '1', '0', '1'],
        ['1', '0', '1', '1', '1', '1', '0', '1', '0', '1'],
        ['1', '0', '0', '0', '0', '0', '0', '0', '0', 'x'],
        ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1']
    ]

    DFS(maze)
