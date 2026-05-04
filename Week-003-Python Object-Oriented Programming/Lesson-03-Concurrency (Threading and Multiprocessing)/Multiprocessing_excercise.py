from multiprocessing import Pool, current_process

def get_square(n):
    res = n * n
    print(f"Worker {current_process().pid} is processing: {n} -> {res}")
    return res

if __name__ == "__main__":
    data = [10, 20, 30, 40]
    with Pool(processes=4) as p:
        final_output = p.map(get_square, data)
    print("\nProcessing complate.")
    print(f"Final results: {final_output}")
