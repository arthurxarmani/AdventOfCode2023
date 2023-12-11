import sys

file = open(sys.argv[1], "r")
lines = file.readlines()

instructions = lines[0].strip()
lines.pop(0)
lines.pop(0)

starting_location = 'AAA' # lines[0].split(" = ")[0]
desired_location = 'ZZZ'
print("starting at: " + starting_location)

maps = {}
for i in range(len(lines)):
    # A line looks like this:
    # AAA = (BBB, CCC)
    lines[i] = lines[i].strip()
    source = lines[i].split()[0]
    left = lines[i].split("(")[1].split(",")[0]
    right = lines[i].split(", ")[1].split(")")[0]
    maps[source] = {'L': left, 'R': right}

print(maps)

steps = 0 
while starting_location != 'ZZZ':
    for idx in range(len(instructions)):
        starting_location = maps[starting_location][instructions[idx]]
        steps += 1

print(steps)