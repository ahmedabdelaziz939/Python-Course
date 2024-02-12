import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Sample data: house size (x) and corresponding prices (y)
house_sizes = np.array([1400, 1600, 1700, 1875, 1100, 1550, 2350, 2450, 1425, 1700])
prices = np.array([245000, 312000, 279000, 308000, 199000, 219000, 405000, 324000, 319000, 255000])

# Reshape the data (required for scikit-learn)
house_sizes = house_sizes.reshape(-1, 1)   # transpose
prices = prices.reshape(-1, 1)             # transpose

# Create a linear regression model
model = LinearRegression()

# Train the model
model.fit(house_sizes, prices)

# Make predictions for new data points
new_house_sizes = np.array([2000, 1800, 1500]).reshape(-1, 1)
predicted_prices = model.predict(new_house_sizes)
print(f"new_house_sizes :{new_house_sizes}")
# Print predicted prices
for i in range(len(new_house_sizes)):
    print(f"Predicted price for a house of size {new_house_sizes[i][0]} sq. ft: ${predicted_prices[i][0]:,.2f}")

# Plot the original data and the regression line
plt.scatter(house_sizes, prices, color='blue', label='Original data')
plt.plot(house_sizes, model.predict(house_sizes), color='red', linewidth=2, label='Linear regression line')
plt.xlabel('House Size (sq. ft)')
plt.ylabel('Price ($)')
plt.legend()
plt.show()