import numpy as np
import pandas as pd

def foo():
    data = pd.read_csv("iris.csv")
    col = "petal_width"
    print(f"Data statistics for column '{col}'")
    print(f"Min value = {min(data[col])}")
    print(f"Max value = {max(data[col])}")
    print(f"Mean value = {np.mean(data[col])}")
    print(f"Mean square error = {np.std(data[col])}")
    print(f"Median = {np.median(data[col])}")
    print(f"Percentile 25 = {np.percentile(data[col],25)}")
    print(f"Percentile 75 = {np.percentile(data[col],75)}")
    return

if __name__ == "__main__":
    foo()