import sys

lines = open(sys.argv[1], 'r').readlines()

inputs = []
for line in lines:
    line = line.strip()
    inputs.append([int(x) for x in line.split()])
    

def parse_differences(input):
    output = []
    cur_idx = 0
    for value in input:
        if cur_idx + 1 < len(input):
            output.append(input[cur_idx + 1] - input[cur_idx])
        cur_idx += 1

    return output

def predict_next_value(diff_rows):
    # start at the bottom row and work upwards
    diff_rows.reverse()
    # append a zero to the first row
    last_val_in_row = 0
    for row in diff_rows:
        row.append(last_val_in_row + row[-1])
        last_val_in_row = row[-1]
        
    return last_val_in_row

# 0 3 6 9 12 15
#  3 3 3 3 3
#   0 0 0 0
# parsing each starting input
extrap_values = []
for row in inputs:
    new_row = row
    diff_rows = [new_row]
    # we want to halt when all values are zero
    while not all(value == 0 for value in new_row):
        # new row is the differences between each previous value
        new_row = parse_differences(new_row)
        diff_rows.append(new_row)
        print(new_row)
    extrap_values.append(predict_next_value(diff_rows))

print(sum(extrap_values))