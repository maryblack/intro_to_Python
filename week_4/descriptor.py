class Value:
    def __init__(self):
        self.value = None

    @staticmethod
    def _commissinon(obj, value):
        return (1-obj.commission)*(value)

    def __get__(self, obj, obj_type):
        return self.value

    def __set__(self, obj, value):
        self.value = self._commissinon(obj, value)


class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission

def main():
    new_account = Account(0.1)
    new_account.amount = 1000

    print(new_account.amount)

if __name__ == '__main__':
    main()