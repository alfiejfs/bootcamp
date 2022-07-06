def calc(operation, x, y):
    if operation == '+':
        return x + y
    elif operation == '-':
        return x - y
    elif operation == 'x':
        return x * y
    elif operation == '/':
        return x / y

def read_data():
    data = []
    with open('data/step_2.txt', 'r') as file:
        for line in file:
            line = line[5:] # Remove "calc "
            split_line = line.split(" ")
            data.append((split_line[0], int(split_line[1]), int(split_line[2])))

    return data


def run():
    total = 0
    for calculation in read_data():
        result = calc(*calculation)
        print(result)
        total += result
    print("Total: " + str(total))

if __name__ == "__main__":
    run()