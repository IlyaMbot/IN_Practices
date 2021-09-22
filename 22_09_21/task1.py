import numpy as np
import pathlib

filepath = pathlib.Path("./lessons")

with open(filepath, "rb") as file2r:
    print("opened", filepath.split('/')[2]) 
    print(file2r.read())
    