from collections import defaultdict, namedtuple

INPUT_PATH = 'input_4'

def read_input():
    with open(INPUT_PATH,'r') as f:
        inp_lst = f.read().split('\n')
        inp = list(filter(None, inp_lst))
        # sort - it will be sorted by date:
        inp.sort()
    return  inp


def get_minute(line):
    min_start = line.find(':') + 1
    min_end = line.find(']')
    return int(line[min_start:min_end])


def get_guard(line):
    guard_start_idx = line.find('#') + 1
    guard_end_idx = line.find(' ', guard_start_idx)
    return int(line[guard_start_idx: guard_end_idx])


def generate_schedule(inp):
    schedule = defaultdict(lambda: defaultdict(int))
    for line in inp:
        minute = get_minute(line)
        if 'Guard' in line:
            guard_id = get_guard(line)
        elif 'falls asleep' in line:
            sleep_minute = minute
        elif 'wakes up' in line:
            for m in range(sleep_minute, minute):
                schedule[guard_id][m] += 1
    return schedule

if __name__ == '__main__':
    inp = read_input()
    schedule = generate_schedule(inp)

    most_sleepy_guard = sorted([(guard, sum(vals.values())) for guard, vals in schedule.items()], key=lambda x:x[1], reverse=True)[0][0]
    most_sleepy_time = sorted(schedule[most_sleepy_guard].items(), key=lambda x:x[1], reverse=True)[0][0]
    print(most_sleepy_guard * most_sleepy_time)

    GuardsData = namedtuple('GuardsData', 'id max_minute count')
    guards_summary =  [
        GuardsData(id,max(guard_schedule, key=guard_schedule.get),max(guard_schedule.values()))
        for id, guard_schedule in schedule.items()
    ]
    record_minute_guard = max(guards_summary, key=lambda x: x.count)
    print(record_minute_guard.id * record_minute_guard.max_minute)

