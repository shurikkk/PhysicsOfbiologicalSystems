import numpy as np

R0 = 3
mu = 0.07

# Fixed point 1
# s_star = 1
# i_star = 0

# Fixed point 2
s_star = 1/R0
i_star = mu/(mu+1) * (1 - 1/R0)

J = np.array(((-R0*i_star-mu, -R0*s_star-mu), (R0*i_star, R0*s_star-1)))
eig = np.linalg.eig(J)
print(J)
print(eig)
print((R0+mu)/(-mu-R0+1))
