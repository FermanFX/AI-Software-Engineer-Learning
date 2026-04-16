import numpy as np

with open('points.data', 'w') as f:
    xs = np.linspace(0, 2*np.pi, 100)
    for x in xs:
        f.write(str(np.cos(x)) + ',' + str(np.sin(x)) + '\n')
