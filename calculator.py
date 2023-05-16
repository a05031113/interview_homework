def calculator_eval(a):
    return eval(a)


def calculator(input):
    input = input.replace(" ", "")

    operands = []
    operators = []

    def apply_operator():
        operator = operators.pop()
        operand2 = operands.pop()
        operand1 = operands.pop()
        if operator == "+":
            result = operand1 + operand2
        elif operator == "-":
            result = operand1 - operand2
        elif operator == "*":
            result = operand1 * operand2
        elif operator == "/":
            result = operand1 / operand2
        operands.append(result)

    index = 0
    while index < len(input):
        if input[index].isdigit():
            start = index
            while index < len(input) and input[index].isdigit():
                index += 1
            operand = int(input[start:index])
            operands.append(operand)
        elif input[index] in "+-*/":
            while operators and operators[-1] in "*/":
                apply_operator()
            operators.append(input[index])
            index += 1
        elif input[index] == "(":
            operators.append(input[index])
            index += 1
        elif input[index] == ")":
            while operators and operators[-1] != "(":
                apply_operator()
            operators.pop()
            index += 1
        else:
            index += 1

    while operators:
        apply_operator()

    return operands[0]


input = "(2+3) * 2"
result = calculator(input)
print("by calculator:", result)
result = calculator_eval(input)
print("by calculator_eval:", result)
