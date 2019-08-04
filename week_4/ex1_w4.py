class PascalList:
    def __init__(self, input_list):
        self.container = input_list
    def __getitem__(self, index):
        return self.container[index-1]

    def __setitem__(self, index, value):
        self.container[index - 1] = value

    def __str__(self):
        return self.container.__str__()


number = PascalList([1,2,3,4])
print(number[4])
number[3] = 333
print(number)