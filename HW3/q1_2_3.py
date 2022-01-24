import numpy as np
import scipy.stats as sp
# import seaborn as sns
import matplotlib.pyplot as plt
# import pandas as pd


data = np.load('yildizHistoRed.npy')
# p_data = pd.DataFrame(data.transpose())
bin_width = 0.5
t = data.transpose()[0]
f = data.transpose()[1]
beta = 1/(np.inner(f, t)/sum(f))
fig = plt.figure()
plt.bar(t, height=f, width=bin_width)
geom_fit = sp.geom.pmf((t+bin_width/2)/bin_width, beta*bin_width)
geom_fit = sum(f)/sum(geom_fit)*geom_fit
plt.plot(t, geom_fit, 'r')
# sns.histplot(x=t, y=f)
plt.xlabel('t [s]')
plt.ylabel('# of measurements')
plt.title('Rescaled exponential distribution fit for myosins taking only 70nm steps')

plt.show()

data = np.load('yildizHistoGreen.npy')
bin_width = 1
t = data.transpose()[0]
f = data.transpose()[1]
beta = 1/(np.inner(f, t)/sum(f))
plt.bar(t, height=f, width=bin_width)
geom_fit = sp.geom.pmf((t+bin_width/2)/bin_width, beta*bin_width)
geom_fit = sum(f)/sum(geom_fit)*geom_fit
plt.plot(t, geom_fit, 'r')
plt.xlabel('t [s]')
plt.ylabel('# of measurements')
plt.title('Rescaled exponential distribution fit for myosins taking(70-x)nm  \nsteps alternating with x nm steps')

plt.show()
