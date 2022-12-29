def frange(start, stop, step):
    r = []
    x = start

    while x <= stop:
        r.append(x)
        x += step

    return r

def decimal_to_minsecs(pace):
    pace_mins = int(pace // 1)
    pace_secs = int(60 * (pace % 1))

    return pace_mins, pace_secs

def main():
    speed_range = frange(6, 15, 0.5)

    for speed in speed_range:
        pace_km = 1/(speed/60)
        pace_mile = pace_km * 1.609344
        pace_km_mins, pace_km_secs = decimal_to_minsecs(pace_km)
        pace_ml_mins, pace_ml_secs = decimal_to_minsecs(pace_mile)

        print(
            f'{speed:>5.2f}km/h = {pace_km_mins:>2}:{pace_km_secs:02d}/km'
            f' = {pace_ml_mins:>2}:{pace_ml_secs:02d}/mile'
        )

        # for spreadsheet
        # print(
        #     f'{speed:>5.2f}km/h;{pace_km_mins:>2}:{pace_km_secs:02d};'
        #     f'{pace_ml_mins:>2}:{pace_ml_secs:02d}'
        # )

if __name__ == "__main__":
    main()