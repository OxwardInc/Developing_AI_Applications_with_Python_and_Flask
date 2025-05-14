def summation(a, b):
    try:
        a = float(a)
        b = float(b)

        result = a + b
        return f'The sum of {a} & {b} is {result}'

    except ValueError:
        return 'Inputs must be numbers only'
    

def substraction(a, b):
    try:
        a = float(a)
        b = float(b)

        result = a - b
        return f"The differences between {a} & {b} is {result}"

    except ValueError:
        return 'Inputs must be numbers only'

def multiplication(a, b):
    try:
        a = float(a)
        b = float(b)

        result = a * b
        return f"The multiplication of {a} & {b} is {result}"

    except ValueError:
        return 'Inputs must be numbers only'
    