# Python implementation of the billion rows challenge
import argparse
import multiprocessing as mp
from itertools import islice
from typing import Any, Generator

import numpy as np
from multiprocessing.spawn import freeze_support


# Generate 1 billion rows of random data
def generate_chunk(stations: list, num_rows: int, seed: float, queue: mp.Queue) -> None:
    np.random.seed(seed)  # Important: unique seed per process
    station_indices = np.random.randint(0, len(stations), size=num_rows)
    values = np.random.uniform(-100, 100, size=num_rows)

    chunk = [f"{stations[i]};{values[j]:.2f}" for j, i in enumerate(station_indices)]
    queue.put("\n".join(chunk) + "\n")

def writer(filename: str, queue: mp.Queue, total_chunks: int) -> None:
    with open(filename, "w", buffering=1024*1024) as f:
        completed = 0
        while completed < total_chunks:
            chunk = queue.get()
            if chunk is None:
                completed += 1
            else:
                f.write(chunk)

def generate(filename: str) -> None:
    print('Reading weather station names')
    with open('weather_stations.csv') as file:
        stations = [n[0] for n in (x.split(';') for x in file.read().splitlines() if not "#" in x)]

    chunk_size = 10_000_000
    total = 1_000_000_000
    num_chunks = total // chunk_size
    num_procs = 8

    queue = mp.Queue(maxsize=num_procs * 2)
    writer_proc = mp.Process(target=writer, args=(filename, queue, num_chunks))
    writer_proc.start()

    print(f'Generating {total:,} rows using {num_procs} workers...')

    processes = []
    for chunk_id in range(num_chunks):
        seed = chunk_id
        p = mp.Process(target=generate_chunk, args=(stations, chunk_size, seed, queue))
        p.start()
        processes.append(p)

        # Limit number of active processes
        if len(processes) >= num_procs:
            for p in processes:
                p.join()
            processes = []

    for p in processes:
        p.join()

    # Signal writer to finish
    for _ in range(num_chunks):
        queue.put(None)

    writer_proc.join()

# Parse given data file to {station=min/avg/max}
def read_file_chunk(filename: str, lines: int =1000) -> Generator[list[str], Any, None]:
    with open(filename, 'r') as file:
        while True:
            chunk = list(islice(file, lines))
            if not chunk:
                break
            yield chunk

def parse(filename: str):
    output_values = {}
    chunk_size = 10_000_000

    for chunk in read_file_chunk(filename, chunk_size):
        for row in chunk:
            split_row = row.split(';')
            if len(split_row) != 2:
                continue
            existing_vals = output_values.get(split_row[0])
            new_value = float(split_row[1])
            if existing_vals is None:
                existing_vals = [1, new_value, new_value, new_value]
            else:
                existing_vals[0] += 1
                existing_vals[1] = max(existing_vals[1], new_value)
                existing_vals[2] = (existing_vals[2] + new_value) / existing_vals[0]
                existing_vals[3] = min(existing_vals[3], new_value)
            output_values[split_row[0]] = existing_vals

    sorted_stations = sorted(output_values.keys())
    output_lines = []
    for station in sorted_stations:
        output_lines.append(f"{station}={output_values[station][1]:.2f}/{output_values[station][2]:.2f}/{output_values[station][3]:.2f}")
    print("{" + ", ".join(output_lines) + "}")

# Main program
if __name__ == '__main__':
    freeze_support()
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str, help='Data file name')
    parser.add_argument('--generate', action="store_true", help='Generate weather data file')
    parser.add_argument('--parse', action="store_true", help='Parse weather data file')
    args = parser.parse_args()

    if args.generate:
        generate(args.filename)
    else:
        parse(args.filename)