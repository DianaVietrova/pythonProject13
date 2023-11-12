import random

class NumberEncryptor:
    def __init__(self, number):
        self.number = number
        self._encrypt()

    def _encrypt(self):

        operation = random.choice(['+', '-', '*'])

        operand = random.randint(1, 10)


        if operation == '+':
            self.result = self.number + operand
        elif operation == '-':
            self.result = self.number - operand
        elif operation == '*':
            self.result = self.number * operand

    def __repr__(self):
        return f"NumberEncryptor: {self.number} -> {self.result}"


if __name__ == "__main__":
    original_number = 35
    encryptor = NumberEncryptor(original_number)

    print(encryptor)
