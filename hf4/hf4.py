# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

# Parameters
delta_t = 1  # Time step in years
years = 10  # Number of years to predict
initial_population = 100  # Initial population
growth_rate_percentage = 5  # Annual growth rate in percentage

# Time array
time = np.arange(0, years + 1, delta_t)

# Population array
population = [initial_population]

# Growth rate calculation and population prediction
for _ in range(years):
    next_population = population[-1] * (1 + growth_rate_percentage / 100)
    population.append(next_population)

# Convert growth rate to an array for plotting
growth_rate = [growth_rate_percentage / 100 * population[i] for i in range(len(population) - 1)]

# Display the predicted population for the next year
print(f"The expected population for the next year's census: {population[1]:.2f}")

# Plot
plt.plot(time, population, 'bo-', label='Population')
plt.plot(time[:-1], growth_rate, 'r--', label='Growth Rate')
plt.xlabel('Time (years)')
plt.ylabel('Population')
plt.legend()
plt.title('Population Growth')
plt.show()
