from sklearn.linear_model import LinearRegression
import numpy as np

def forecast_kpi(df):
    X = np.array(range(len(df))).reshape(-1, 1)
    y = df.iloc[:, 1].values
    model = LinearRegression().fit(X, y)
    next_val = model.predict([[len(X)]])[0]
    return round(next_val, 2)