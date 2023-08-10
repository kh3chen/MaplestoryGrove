with open('input.txt', 'r') as f:
    lines = f.readlines()

output = ''
prev_num = None
for line in lines:
    num, id_ = line.strip().split('\t')
    if num != prev_num:
        if prev_num is not None:
            output += '\n'
        output += f'{num} '
    output += f'{id_} '
    prev_num = num

with open('output.txt', 'w') as f:
    f.write(output)
