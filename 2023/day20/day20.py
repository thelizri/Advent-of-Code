from collections import deque
from math import lcm

example_input = r"""broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a""".splitlines()

example_input2 = r"""broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output""".splitlines()

input = open("day20.txt").read().splitlines()

# (to, signal, from)
signal_queue = deque()


class Module:
    def __init__(self, name, type, value=0, outputs=[], inputs=None):
        self.name = name
        if type == "%":
            self.type = "FLIPFLOP"
        elif type == "&":
            self.type = "NAND"
        elif type == "broadcaster":
            self.type = "BROADCAST"
        else:
            self.type = "OUTPUT"
        self.outputs = outputs
        self.value = value

        if inputs is None:
            self.inputs = {}
        else:
            self.inputs = inputs

    def receive_signal(self, signal, source):
        if self.type == "FLIPFLOP":
            self.flip_flop(signal)
        elif self.type == "NAND":
            self.nand(signal, source)
        elif self.type == "BROADCAST":
            self.broadcast(signal)

    def send_signal(self, signal):
        for destination in self.outputs:
            signal_queue.append((destination, signal, self.name))

    def flip_flop(self, signal):
        if signal == 0:  # Only Flips on low signal
            self.value = 1 if self.value == 0 else 0
            self.send_signal(self.value)

    def nand(self, signal, source):
        self.inputs[source] = signal
        if all(self.inputs.values()):
            self.value = 0
        else:
            self.value = 1
        self.send_signal(self.value)

    def broadcast(self, signal):
        self.value = signal
        self.send_signal(self.value)

    def __str__(self):
        return f"{self.name} {self.type} {self.value} {self.inputs} {self.outputs}"


def parse_input(input):
    modules = {}
    for row in input:
        broadcaster, receivers = row.split(" -> ")
        receivers = [r.strip() for r in receivers.split(",")]
        if broadcaster[0] in "%&":
            type = broadcaster[0]
            broadcaster = broadcaster[1:]
            modules[broadcaster] = Module(broadcaster, type, outputs=receivers)
        else:
            modules[broadcaster] = Module(broadcaster, broadcaster, outputs=receivers)

    for module in modules.values():
        if module.type == "NAND":
            for possible_input_module in modules.values():
                if possible_input_module.name == module.name:
                    continue
                if module.name in possible_input_module.outputs:
                    module.inputs[possible_input_module.name] = 0
    return modules


def part1(input):
    modules = parse_input(input)
    low, high = 0, 0
    # Press button
    for i in range(1000):
        signal_queue.append(("broadcaster", 0, "button"))
        while signal_queue:
            destination, signal, source = signal_queue.popleft()
            if signal == 1:
                high += 1
            else:
                low += 1
            if destination in modules:
                modules[destination].receive_signal(signal, source)

    answer = high * low
    print("Part 1:", answer)


part1(input)

# Part 2
# rx is being fed into by one module
# that module is being fed by several modules
# those modules all need to signal high
# find the cycle for each of those modules, we're assuming there is a cycle


def part2(input):
    modules = parse_input(input)
    (module_that_pumps_into_rx,) = [
        module for module in modules.values() if "rx" in module.outputs
    ]

    find_cycles_for_these_modules = list(module_that_pumps_into_rx.inputs.keys())
    cycles = []
    button_presses = 0
    while find_cycles_for_these_modules:
        button_presses += 1
        signal_queue.append(("broadcaster", 0, "button"))
        while signal_queue:
            destination, signal, source = signal_queue.popleft()
            if destination in modules:
                modules[destination].receive_signal(signal, source)

            if signal == 1 and source in find_cycles_for_these_modules:
                cycles.append(button_presses)
                find_cycles_for_these_modules.remove(source)

    answer = lcm(*cycles)
    print("Part 2:", answer)


part2(input)
