import re
from collections import Counter

class ArrayList:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.array = [None] * capacity
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def get_entry(self, pos):
        if 0 <= pos < self.size:
            return self.array[pos]
        else:
            return None

    def insert(self, pos, e):
        if not self.is_full() and 0 <= pos <= self.size:
            for i in range(self.size, pos, -1):
                self.array[i] = self.array[i - 1]
            self.array[pos] = e
            self.size += 1

    def delete(self, pos):
        if 0 <= pos < self.size:
            for i in range(pos, self.size - 1):
                self.array[i] = self.array[i + 1]
            self.array[self.size - 1] = None
            self.size -= 1

    def replace(self, pos, e):
        if 0 <= pos < self.size:
            self.array[pos] = e

    def __str__(self):
        return str(self.array[:self.size])

class LineEditor:
    def __init__(self):
        self.lines = ArrayList(1000)

    def insert(self, pos, line):
        self.lines.insert(pos, line)

    def make_dictionary(self):
        all_text = ' '.join(self.lines.get_entry(i) for i in range(self.lines.size))
        words = re.findall(r'\b\w+\b', all_text)
        word_count = Counter(words)

        print("입력된 내용 :", all_text)
        for word, count in word_count.items():
            print(f"{word} : {count}")

        with open('dic.txt', 'w') as file:
            for word, count in word_count.items():
                file.write(f"{word} : {count}\n")

if __name__ == "__main__":
    editor = LineEditor()
    while True:
        command = input("[메뉴선택] i-입력, d-삭제, r-변경, p-출력, l-파일읽기, s-저장, q-종료, m-사전생성 => ")

        if command == 'i':
            pos = int(input("  입력할 행 번호: ")) - 1
            line = input("  입력행 내용: ")
            editor.insert(pos, line)

        elif command == 'd':
            pos = int(input("  삭제행 번호: ")) - 1
            editor.lines.delete(pos)

        elif command == 'r':
            pos = int(input("  변경행 번호: ")) - 1
            new_line = input("  변경행 내용: ")
            editor.lines.replace(pos, new_line)

        elif command == 'p':
            print('Line Editor')
            for line in range(editor.lines.size):
                print(f'[{line + 1:2d}] {editor.lines.get_entry(line)}')
            print()

        elif command == 'l':
            filename = 'test.txt'
            with open(filename, "r") as infile:
                lines = infile.readlines()
                for line in lines:
                    editor.lines.insert(editor.lines.size, line.rstrip('\n'))

        elif command == 's':
            filename = 'test.txt'
            with open(filename, "w") as outfile:
                for i in range(editor.lines.size):
                    outfile.write(editor.lines.get_entry(i) + '\n')

        elif command == 'm':
            editor.make_dictionary()

        elif command == 'q':
            break
