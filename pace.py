import sys

def args_present(args):
    arg_count = len(args)
    count_correct = True if arg_count == 3 else False

    return count_correct

def range_valid(start, end):
    if end > start:
        return start, end
    else:
        return False

def step_positive(step_size):
    step_size = step_size if step_size > 0 else False

    return step_size

def process_args(args):
    if args_present(args):
        start, end, step_size = args
    else:
        print('missing args, using defaults')
        start = 6
        end = 15
        step_size = 0.5

    start, end = range_valid(start, end) or exit('invalid range')
    step_size = step_positive(step_size) or exit('step must be positive')

    return start, end, step_size

def frange(start, end, step_size):
    range = []
    x = start

    while x <= end:
        range.append(x)
        x += step_size

    return range

def decimal_to_minsecs(pace):
    pace_mins = int(pace // 1)
    pace_secs = int(60 * (pace % 1))

    return pace_mins, pace_secs

def main():
    KMS_PER_MILE = 1.609344

    # convert args to float, also removes entry point in pos [0]
    args = [float(x) for x in sys.argv[1:]]
    start, end, step_size = process_args(args)
    speed_range = frange(start, end, step_size)
    output_rows = []

    for speed in speed_range:
        pace_km = 1/(speed/60)
        pace_mile = pace_km * KMS_PER_MILE
        pace_km_mins, pace_km_secs = decimal_to_minsecs(pace_km)
        pace_ml_mins, pace_ml_secs = decimal_to_minsecs(pace_mile)

        output_rows.append([
            f'{speed:.2f}', 
            f'{pace_km_mins}:{pace_km_secs:02d}', 
            f'{pace_ml_mins}:{pace_ml_secs:02d}'
            ])

    for row in output_rows:
        print(f'{row[0]:>5}km/h = {row[1]:>5}/km = {row[2]:>5}/mile') # for screen
        # print(f'{row[0]:>5}km/h;{row[1]:>5};{row[2]:>5}') # ;-separated for spreadsheet
    
if __name__ == "__main__":
    main()
    