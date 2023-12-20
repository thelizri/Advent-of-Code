from collections import deque

input = r"""broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output""".splitlines()

input = open("day20.txt").read().splitlines()

# % = flip flop, & = nand, # broadcaster sends input to all receivers
signal_queue = deque()
modules = {}

# module = {"type": type, "receiver": [], "value": value}, default value is 0
high, low = 0, 0
modules["output"] = {"type": "output", "receiver": [], "value": 0}


def parse_input(input):
    for row in input:
        left, right = row.split(" -> ")
        receiver = right.split(", ")
        inputs = None
        if left[0] == "%":
            type = "%"
            value = 0
            name = left[1:]
        elif left[0] == "&":
            type = "&"
            value = 1
            name = left[1:]
            inputs = {}
            for row in input:
                left, right = row.split(" -> ")
                if name in right:
                    left = left if left == "broadaster" else left[1:]
                    inputs[left] = 0
        else:
            type = "broadcaster"
            name = left
            value = 0
        if inputs:
            modules[name] = {
                "type": type,
                "receiver": receiver,
                "value": value,
                "name": name,
                "inputs": inputs,
            }
        else:
            modules[name] = {
                "type": type,
                "receiver": receiver,
                "value": value,
                "name": name,
            }


def flip_value(value):
    return 1 if value == 0 else 0


def increment_counter(signal):
    global high, low
    if signal == 1:
        high += 1
    else:
        low += 1


def interpret_signal(signal, wire):
    if wire == "output":
        return None

    module = modules[wire]
    type = module["type"]
    if type == "%":
        # Flips value if signal is 0
        if signal == 0:
            module["value"] = flip_value(module["value"])
        else:
            return None
    elif type == "&":
        values = module["inputs"].values()
        if all(values):
            module["value"] = 0
        else:
            module["value"] = 1
    elif type == "broadcaster":
        module["value"] = signal

    # Send signal to receivers
    for receiver in module["receiver"]:
        increment_counter(module["value"])
        if receiver in modules:
            signal_queue.append((module["value"], receiver))
            if modules[receiver]["type"] == "&":
                modules[receiver]["inputs"][wire] = module["value"]


def press_button():
    increment_counter(0)
    signal_queue.append((0, "broadcaster"))
    while signal_queue:
        signal, wire = signal_queue.popleft()
        interpret_signal(signal, wire)


parse_input(input)
for i in range(1000):
    press_button()
result = high * low
print("Result: {}".format(result))
