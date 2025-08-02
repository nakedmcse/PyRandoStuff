# Python implementation of the billion rows challenge
import argparse
import multiprocessing as mp
from multiprocessing.spawn import freeze_support

import numpy as np

# Generate 1 billion rows of random data
def generate_chunk(stations, num_rows, seed, queue):
    np.random.seed(seed)  # Important: unique seed per process
    station_indices = np.random.randint(0, len(stations), size=num_rows)
    values = np.random.uniform(-100, 100, size=num_rows)

    chunk = [f"{stations[i]};{values[j]:.2f}" for j, i in enumerate(station_indices)]
    queue.put("\n".join(chunk) + "\n")

def writer(filename, queue, total_chunks):
    with open(filename, "w", buffering=1024*1024) as f:
        completed = 0
        while completed < total_chunks:
            chunk = queue.get()
            if chunk is None:
                completed += 1
            else:
                f.write(chunk)

def generate(filename: str):
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
def parse(filename: str):
    pass

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