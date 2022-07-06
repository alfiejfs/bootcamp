def calc(operation, x, y):
    if operation == '+':
        return x + y
    elif operation == '-':
        return x - y
    elif operation == 'x':
        return x * y
    elif operation == '/':
        return x / y

def get_data():
    with open('data/step_4.txt', 'r') as file:
        return [line.strip() for line in file]

def get_next_instruction(last_instruction, data):
    if last_instruction == -1:
        return 0
    else:
        split = data[last_instruction].rstrip().split(" ")
        if split[0] == "goto":
            if split[1] == "calc":
                return int(calc(split[2], int(split[3]), int(split[4])))
            else:
                return int(split[1])
        elif split[0] == "remove":
            index = int(split[1])
            if len(data) > index:
                del data[int(split[1])]
            return last_instruction + 1
        elif split[0] == "replace":
            index_one, index_two = int(split[1]), int(split[2])
            if len(data) > max(index_one, index_two):
                data[index_one] = data[index_two]
            return last_instruction + 1

def run():
    seen = []
    data = get_data()
    instruction = get_next_instruction(-1, data)
    while data[instruction] not in seen:
        seen.append(data[instruction])
        instruction = get_next_instruction(instruction, data)

    print("Instruction: " + data[instruction])
    print("Line: " + str(instruction))


if __name__ == "__main__":
    run()