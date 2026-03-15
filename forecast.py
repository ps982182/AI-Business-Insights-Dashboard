from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd

def forecast_sales(df):

    monthly = df.groupby("month")["sales"].sum().reset_index()

    X = np.arange(len(monthly)).reshape(-1,1)
    y = monthly["sales"]

    model = LinearRegression()
    model.fit(X,y)

    future_months = np.arange(len(monthly), len(monthly)+3).reshape(-1,1)
    forecast = model.predict(future_months)

    forecast_df = pd.DataFrame({
        "month":[f"Future_{i}" for i in range(1,4)],
        "sales":forecast
    })

    return forecast_df