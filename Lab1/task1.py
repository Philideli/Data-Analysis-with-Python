import numpy as np

def run():
    arr = np.arange(1,3,0.2)
    print(f"1. An array from 1 to 3  (excluding 'to') with a step 0.2 {arr}")

    arr = np.ones([3,3], dtype=int)
    print(f"2. An array of 1s 3x3 {arr}")

    arr = np.zeros([3,4], dtype=int)
    print(f"3. An array of zeros 3x3 {arr}")

    arr = np.linspace(10,1,5)
    print(f"4. An array of evenly destributed 5 floats between 10 and 1 {arr}")

    arr = np.random.random([3,3])
    print(f"5. [RANDOM] 3x3 array of random floats between 0 and 1 {arr}")

    arr = np.random.randint(1,90,[3,3])
    print(f"6. [RANDOM] 3x3 array of random ints between 1 and 90  (excluding 'to') {arr}")

    arr = np.empty(10)
    print(f"7. [SEMI-RANDOM] Semi-random array of 10 elements. Only reads data on call {arr}")
    return