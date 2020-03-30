class StdInputOutput():

    def print(self, msg):
        print(msg)

    def input(self, msg):
        return input(msg)


class InputOutputForTest():
    def __init__(self, instructions):
        self.output = []
        self.instructions = instructions

    def print(self, msg):
        self.output.append(msg)

    def input(self, msg):
        return self.instructions.pop(0)


