import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('../data/daily_product_demand.csv')
df['Date'] = pd.to_datetime(df['Date'])

# Forecast for a single product (example)
product_df = df[df['Product ID'] == 'P1001'].groupby('Date')['Units Sold'].sum()
model = ARIMA(product_df, order=(5,1,0))
model_fit = model.fit()
forecast = model_fit.forecast(steps=30)

# Plot
plt.plot(product_df[-60:], label='Historical')
plt.plot(forecast, label='Forecast', linestyle='--')
plt.legend()
plt.title('30-Day Forecast for Product P1001')
plt.show()
