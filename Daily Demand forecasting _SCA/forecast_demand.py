import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('../data/daily_product_demand.csv')
df['Date'] = pd.to_datetime(df['Date'])

# Prepare data for Prophet
product_df = df[df['Product ID'] == 'P1001']
daily_demand = product_df.groupby('Date')['Units Sold'].sum().reset_index()
daily_demand.columns = ['ds', 'y']  # Prophet requires these column names

# Build and fit the model
model = Prophet()
model.fit(daily_demand)

# Create future dataframe
future = model.make_future_dataframe(periods=30)
forecast = model.predict(future)

# Plot forecast
model.plot(forecast)
plt.title('Prophet Forecast – Product P1001')
plt.xlabel('Date')
plt.ylabel('Units Sold')
plt.show()

