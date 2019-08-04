import tempfile
import os
from pprint import pprint


class File:
    def __init__(self, full_path):
        self.path = full_path

    @property
    def content(self):
        with open(self.path, 'r') as f:
            return f.readlines()

    def write(self, str):
        with open(self.path, 'w') as f:
            f.write(str)
        return File(self.path)

    def __add__(self, obj):
        path = os.path.join(tempfile.gettempdir(),'new_file.txt')
        with open(path, 'w') as f:
            f.write(''.join(self.content))
            f.write(''.join(obj.content))
        return File(path)

    def __getitem__(self, item):
        return self.content[item]

    def __repr__(self):
        return f'{self.path}'

def main():
    path_1 = 'C:\\Users\Admin\PycharmProjects\intro_to_Python\week_4\\file_1.txt'
    path_2 = 'C:\\Users\Admin\PycharmProjects\intro_to_Python\week_4\\file_2.txt'
    file_1 = File(path_1)
    file_1.write('new\ncontent')
    file_2 = File(path_2)
    for line in file_1.write('wtf\ni`m\ndoing\n')+file_2.write('with\nmy\nlife\n'):
        pprint(line)



if __name__ == "__main__":
    main()
