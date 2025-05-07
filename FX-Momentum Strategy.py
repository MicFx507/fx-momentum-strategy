import numpy as np
import pandas as pd

# Simulate dummy EUR/USD prices
np.random.seed(42)
dates = pd.date_range(start='2024-01-01', periods=100, freq='D')
prices = 1.05 + np.cumsum(np.random.normal(0, 0.001, 100))

# Calculate returns using np.diff
returns = np.diff(prices) / prices[:-1]

# Create DataFrame
df = pd.DataFrame({
    'Date': dates[1:],  # skip first date (diff shortens length)
    'Price': prices[1:],
    'Return': returns
})
df.set_index('Date', inplace=True)

# Generate signal: 1 if last 3 returns were all positive
df['Signal'] = (df['Return'] > 0).rolling(3).sum() == 3
df['Signal'] = df['Signal'].astype(int)

# Save to CSV
df.to_csv('eurusd_momentum_strategy.csv')
