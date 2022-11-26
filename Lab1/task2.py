import numpy as np

def foo():
    arr = np.arange(0,20)
    print(f"An array from 0 to 20  (excluding 'to'){arr}")
    print(f"Regular indexing {arr[0]}, {arr[7]}")
    print(f"Negative indexing (reversed order) {arr[-1]}, {arr[-5]}") 
    print(f"Slicing array with [from:to:step] (excluding 'to') {arr[2:7:2]}")
    print(f"Slice hack for easy array revesion {arr[::-1]}")
    return

if __name__ == "__main__":
    foo()