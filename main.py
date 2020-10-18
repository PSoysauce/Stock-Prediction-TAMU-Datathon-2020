import sys
import numpy as np
from agent import Agent

a = None
for line in sys.stdin:
    row = line.split(',')
    row = np.array([float(x.strip()) for x in row])
    if not a:
        a = Agent()

    res = a.step(row)
    print(f"{res[0].name} {res[1]}")
