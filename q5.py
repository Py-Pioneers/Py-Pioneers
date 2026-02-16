#Team name : Py-Pioneers
def calculate(expression: str) -> float:
    nums, num, op = [], 0, '+'
    expression = expression.replace(" ", "") + '+'
    for ch in expression:
        if ch.isdigit():
            num = num * 10 + int(ch)
        else:
            if op == '+': nums.append(num)
            elif op == '-': nums.append(-num)
            elif op == '*': nums[-1] *= num
            elif op == '/': nums[-1] /= num
            num, op = 0, ch
    return round(sum(nums), 2)
