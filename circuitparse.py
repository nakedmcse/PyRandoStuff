# Warmup 2 Part 1
def replace_logic(oper: str) -> str:
    oper = oper.replace("OR", "|").replace("AND", "&").replace("NOT", "~")
    oper = oper.replace("LSHIFT", "<<").replace("RSHIFT", ">>")
    oper = oper.replace("in", "inn").replace("as", "ass").replace("is", "iss").replace("if", "iff")
    return oper


with open('circuit.txt') as file:
    gates = [[y[1], y[0]] for y in (x.split(' -> ') for x in file.read().splitlines())]

gates.sort(key=lambda x: len(x[1].split(' ')), reverse=True)
#print(gates)

dep_sorted_gates = []
insert = gates.pop(0)
insert[1] = replace_logic(insert[1])
dep_sorted_gates.append(insert)
for gate in gates:
    found = False
    gate[0] = replace_logic(gate[0])
    gate[1] = replace_logic(gate[1])
    for i in range(len(dep_sorted_gates)):
        if gate[0]+' ' in dep_sorted_gates[i][1]:
            dep_sorted_gates.insert(i, gate)
            found = True
            break
    if not found:
        dep_sorted_gates.append(gate)

commands = [f'{x[0]} = {x[1]}' for x in dep_sorted_gates]
commands.append('print(a)')
print(commands)

for command in commands:
    try:
        exec(command)
    except:
        continue

