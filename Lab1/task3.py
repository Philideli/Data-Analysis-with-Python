import numpy as np

def foo():
    print("")
    arr = np.arange(0,20)
    print(f"An array from 0 to 20 (excluding 'to'){arr}")
    print(f"Every value + 5 {arr+5}")
    print(f"Every value * 5 {arr*5}")
    print(f"Every value power of 4 {arr**4}")
    print(f"Sum of values {np.add.reduce(arr)}")
    print(f"Sum of values (with steps) {np.add.accumulate(arr)}")
    print(f"Create 0-9 multiplication table {np.multiply.outer(arr, arr)}")
    return

if __name__ == "__main__":
    foo()