class MyStack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        if self.stack:
            return False
        return True

    def push(self, elem):
        self.stack.append(elem)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)


def check_brackets(brackets: str) -> str:
    if len(brackets) % 2 != 0 or brackets[0] in ']})':
        return 'Несбалансированно'
    verifiation_dict = {'(': ')', '[': ']', '{': '}'}
    stack = MyStack()
    for bracket in brackets:
        if bracket in verifiation_dict:
            stack.push(bracket)
        elif bracket in verifiation_dict.values():
            if not stack.is_empty() and bracket == verifiation_dict.get(stack.peek()):
                stack.pop()
            else:
                return 'Несбалансированно'

    if stack.is_empty():
        return 'Сбалансированно'
    else:
        return 'Несбалансированно'
