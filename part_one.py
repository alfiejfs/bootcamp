def calc(x, y, operation):
    if operation == '+':
        return x + y
    elif operation == '-':
        return x - y
    elif operation == 'x':
        return x * y
    elif operation == '/':
        return x / y

def get_inputs():
    operation = input("Enter operation: ")
    x = int(input("Enter number 1: "))
    y = int(input("Enter number 2: "))

    return x, y, operation

def run():
    x, y, operation = get_inputs()
    print(calc(operation, x, y))

if __name__ == "__main__":
    run()