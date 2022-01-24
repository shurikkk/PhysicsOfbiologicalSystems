import numpy as np
# import scipy.stats as sp
# import seaborn as sns
import matplotlib.pyplot as plt
# import pandas as pd


data = np.load('yildizHistoRed.npy')
# p_data = pd.DataFrame(data.transpose())
bin_width = 0.5
t = data.transpose()[0]
f = data.transpose()[1]
beta = 1/(np.inner(f, t)/(2*sum(f)))
fig = plt.figure()
# sns.barplot(data=p_data, color='b')
plt.bar(t, height=f, width=bin_width)
# plt.plot(t, beta*np.exp(-t*beta))
# pois_fit = sp.poisson.pmf((t+bin_width/2)/bin_width, beta*bin_width)
conv_fit = beta**2*t*np.exp(-beta*t)
conv_fit = sum(f)/sum(conv_fit)*conv_fit
plt.plot(t, conv_fit, 'r')
# sns.histplot(x=t, y=f)
plt.xlabel('t [s]')
plt.ylabel('# of measurements')
plt.title('Rescaled distribution of convolution of two exponential distributions \n'
          'for myosins taking only 70nm steps')

plt.show()

data = np.load('yildizHistoGreen.npy')
# p_data = pd.DataFrame(data.transpose())
bin_width = 1
t = data.transpose()[0]
f = data.transpose()[1]
beta = 1/(np.inner(f, t)/(2*sum(f)))
plt.bar(t, height=f, width=bin_width)
conv_fit = beta**2*t*np.exp(-beta*t)
conv_fit = sum(f)/sum(conv_fit)*conv_fit
plt.plot(t, conv_fit, 'r')
# sns.histplot(x=t, y=f)
plt.xlabel('t [s]')
plt.ylabel('# of measurements')
plt.title('Rescaled distribution of convolution of two exponential distributions\n '
          'for myosins taking(70-x)nm steps alternating with x nm steps')

plt.show()
