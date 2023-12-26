from collections import deque

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

    def receive_signal(self, signal, broadcaster):
        if self.type == "FLIPFLOP":
            self.flip_flop(signal)
        elif self.type == "NAND":
            self.nand(signal, broadcaster)
        elif self.type == "BROADCAST":
            self.broadcast(signal)

    def send_signal(self, signal):
        for output in self.outputs:
            signal_queue.append((output, signal, self.name))

    def flip_flop(self, signal):
        if signal == 0:  # Only Flips on low signal
            self.value = 1 if self.value == 0 else 0
            self.send_signal(self.value)

    def nand(self, signal, broadcaster):
        self.inputs[broadcaster] = signal
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
        receivers = receivers.split(", ")
        if broadcaster[0] in "%&":
            type = broadcaster[0]
            broadcaster = broadcaster[1:]
            module = Module(broadcaster, type, outputs=receivers)
            modules[broadcaster] = module
            if module.type == "NAND":
                for possible_input_module in modules.values():
                    if possible_input_module.name == module.name:
                        continue
                    if module.name in possible_input_module.outputs:
                        module.inputs[possible_input_module.name] = 0
        else:
            modules[broadcaster] = Module(broadcaster, broadcaster, outputs=receivers)
    return modules


modules = parse_input(example_input2)

low, high = 0, 0
# Press button
for i in range(1000):
    signal_queue.append(("broadcaster", 0, "button"))
    while signal_queue:
        wire, signal, broadcaster = signal_queue.popleft()
        if signal == 1:
            high += 1
        else:
            low += 1
        if wire in modules:
            modules[wire].receive_signal(signal, broadcaster)

answer = high * low
print("Part 1:", answer)
