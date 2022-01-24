import numpy as np
# import seaborn as sns
import matplotlib.pyplot as plt
# import pandas as pd


data = np.load('yildizHistoRed.npy')
# p_data = pd.DataFrame(data.transpose())
bin_width = 0.5
t = data.transpose()[0]
f = data.transpose()[1]
fig = plt.figure()
# sns.barplot(data=p_data, color='b')
plt.bar(t, height=f, width=bin_width)
# sns.histplot(x=t, y=f)
plt.xlabel('t [s]')
plt.ylabel('# of measurements')
plt.title('Stepping frequency histogram for myosins taking only 70nm steps')

plt.show()

data = np.load('yildizHistoGreen.npy')
# p_data = pd.DataFrame(data.transpose())
bin_width = 1
t = data.transpose()[0]
f = data.transpose()[1]
# fig = plt.figure()
# sns.barplot(data=p_data, color='b')
plt.bar(t, height=f, width=bin_width)
# sns.histplot(x=t, y=f)
plt.xlabel('t [s]')
plt.ylabel('# of measurements')
plt.title('Stepping frequency histogram for myosins taking(70-x)nm  \nsteps alternating with x nm steps')

plt.show()
