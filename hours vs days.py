import matplotlib.pyplot as plt

# Define data
hours = [3, 3, 3, 3, 4, 3, 2, 2, 3, 2, 4, 3, 3, 3, 2, 4, 2, 2, 2, 1, 2, 1, 1, 3, 2, 2, 3, 2, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 3, 3, 2, 3, 1, 2, 2, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 2, 2, 1, 1 ]
days = list(range(0, 60))
# Define colors based on hours
colors = ['red' if h == 1 else 'green' if h == 4 else 'blue' if h == 3 else 'orange' for h in hours]
# Plot the data
plt.title('Hours spent on learning')
plt.xlabel('Days')
plt.ylabel('Hours')
plt.bar(days, hours, color=colors)
plt.show()