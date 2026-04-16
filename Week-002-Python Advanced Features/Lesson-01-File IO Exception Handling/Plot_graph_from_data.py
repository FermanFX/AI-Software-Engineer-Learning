import matplotlib.pyplot as plt

import pandas as pd
import numpy as np

days = np.arange(1, 366)
sales = np.random.normal(55000, 15000, 365) 

df = pd.DataFrame({'days': days, 'gross': sales})
df.to_csv('sales.csv', index=False, header=False)

x, y = [], []

with open('sales.csv', 'r') as f:
    lines = f.readlines()
    for line in lines:
        data = line.split(',')
        x.append(int(data[0]))
        y.append(float(data[1]))


plt.figure()
plt.plot(x, y)
plt.xlabel('days')
plt.ylabel('gross')
plt.title('Sales / year')


plt.figure()
plt.hist(y, bins=30)
plt.title('Histogram - sales / year')

plt.show()
