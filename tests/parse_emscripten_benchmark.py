from collections import defaultdict
import sys
import re

grid = defaultdict(list)

bench_name = ''
bench_names = []
engine_names = []

found_all_engines = False

for line in file(sys.argv[1]):
    if line.startswith('test_'):
        bench_name = line[5:].split(' ')[0]
        bench_names.append(bench_name)
        continue

    match = re.match('^\s*([\w-]+): mean: (\d+.\d+)', line)
    if match:
        if match.group(1) not in engine_names:
            engine_names.append(match.group(1))
            assert not found_all_engines
        else:
            found_all_engines = True

        grid[bench_name].append(match.group(2))

print('engine,' + ','.join(bench_names))

for e, engine_name in enumerate(engine_names):
    row = engine_name
    for bench_name in bench_names:
        if not grid[bench_name]:
            row += ',0.0'
        else:
            row += ',' + grid[bench_name][e]
    print(row)
