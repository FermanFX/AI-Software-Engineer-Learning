import matplotlib.pyplot as plt

with open('points.data', 'r') as f:
    lines = f.readlines()

x, y = [], []
for line in lines:
    # Convert comma-separated string back to floats
    point = [float(i) for i in line.strip().split(',')]
    x.append(point[0])
    y.append(point[1])

plt.plot(x, y)
plt.axis('equal')
plt.show()
