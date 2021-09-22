import numpy as np

filepath = "./lessons/0nyb1470.17d.Z"

with open(filepath, "rb") as file2r:
    print("opened", filepath.split('/')[2]) 
    print(file2r.read())
    