class Expression:
    def __init__(self, expression):
        self.expression = expression

    def compute(self):
        try:
            return eval(self.expression)
        except Exception as e:
            return f"Error: {e}"

class Variable:
    def __init__(self, name):
        self.name = name
        self.value = None

    def set_value(self, value):
        self.value = value

    def __str__(self):
        return f"Variable(name={self.name}, value={self.value})"

