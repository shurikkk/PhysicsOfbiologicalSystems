p_plus_sick = 0.7
p_minus_sick = 1 - p_plus_sick
p_minus_healthy = 0.9
p_plus_healthy = 1 - p_minus_healthy

# p_sick = 0.9
p_sick = 0.5
p_healthy = 1 - p_sick

p_plus = p_plus_healthy*p_healthy + p_plus_sick*p_sick
p_minus = p_minus_healthy*p_healthy + p_minus_sick*p_sick

p_pmpmp_naive = p_plus**3 * p_minus**2
p_pmpmp = p_plus_healthy**3 * p_minus_healthy**2 * p_healthy + \
          p_plus_sick**3 * p_minus_sick**2 * p_sick

p_healthy_pmpmp = (p_plus_healthy**3 * p_minus_healthy**2 * p_healthy)/p_pmpmp
p_sick_pmpmp = (p_plus_sick**3 * p_minus_sick**2 * p_sick)/p_pmpmp

p_healthy_plus = (p_plus_healthy * p_healthy)/p_plus
p_sick_plus = (p_plus_sick * p_sick)/p_plus

print('p(sick|+-+-+): ', p_sick_pmpmp)
