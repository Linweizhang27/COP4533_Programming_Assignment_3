import time
import matplotlib.pyplot as plt
from Algorithm import find_max_value, find_subsequence
from main import parse_file

def measure_time(filename):
    val, A, B = parse_file(filename)

    start = time.perf_counter()

    max_val, M = find_max_value(val, A, B)
    path = find_subsequence(M, val, A, B)

    end = time.perf_counter()

    t = end - start
    size = len(A) * len(B) #the 2d table

    return t, size


def main():
    files = [f"data/input{i}.in" for i in range(1, 11)]
    times = []
    sizes = []

    for file in files:
        t, size = measure_time(file)
        times.append(t)
        sizes.append(size)

        print(f"{file}: {t:.6f}s, size: {size}")

    paired = sorted(zip(sizes, times))
    sizes, times = zip(*paired)

    plt.plot(sizes, times, marker="o") #plotting it against len(A) * len(B) should give me a straight line
    plt.xlabel("len(A) * len(B)")
    plt.ylabel("time")
    plt.show()


if __name__ == "__main__":
    main()