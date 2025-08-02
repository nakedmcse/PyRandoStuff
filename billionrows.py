# Python implementation of the billion rows challenge
import argparse, random
import numpy as np

# Generate 1 billion rows of random data
def generate(filename: str):
    print('Reading weather station names')
    with open('weather_stations.csv') as file:
        stations = [n[0] for n in (x.split(';') for x in file.read().splitlines() if not "#" in x)]

    station_count = len(stations)
    chunk_size = 10_000_000
    total = 1_000_000_000
    progress_bar_size = 40

    print('Generation Progress:', end='', flush=True)
    progress = 0

    with open(filename, "w", buffering=1024*1024) as file:
        for i in range(0, total, chunk_size):
            current_chunk = min(chunk_size, total - i)

            station_indices = np.random.randint(0, station_count, size=current_chunk)
            values = np.random.uniform(-100, 100, size=current_chunk)

            lines = [f'{stations[station_indices[j]]};{values[j]:.2f}' for j in range(current_chunk)]
            file.write("\n".join(lines) + "\n")

            new_progress = int((i + current_chunk) / total * progress_bar_size)
            while progress < new_progress:
                print('#', end='', flush=True)
                progress += 1

    print()

# Parse given data file to {station=min/avg/max}
def parse(filename: str):
    pass

# Main program
parser = argparse.ArgumentParser()
parser.add_argument('filename', type=str, help='Data file name')
parser.add_argument('--generate', action="store_true", help='Generate weather data file')
parser.add_argument('--parse', action="store_true", help='Parse weather data file')
args = parser.parse_args()

if args.generate:
    generate(args.filename)
else:
    parse(args.filename)