time = '1h 45m,360s,25m,30m 120s,2h 60s'

time_splits = time.split(',')

time_min = 0

print(time_splits) #['1h 45m', '360s', '25m', '30m 120s', '2h 60s']

for time_split in time_splits:
    parts = time_split.split()
    for part in parts:
        if 'h' in part:
            hours = int(part.replace('h', ''))
            time_min += hours * 60
        elif 'm' in part:
            minutes = int(part.replace('m', ''))
            time_min += minutes
        elif 's' in part:
            seconds = int(part.replace('s', ''))
            time_min += seconds / 60


print(time_min)
