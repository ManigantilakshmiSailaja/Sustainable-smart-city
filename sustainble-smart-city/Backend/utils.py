import pandas as pd
from sklearn.linear_model import LinearRegression
from io import StringIO

# MOCK LLM function
def summarize_text(text):
    return f"Summary: {text[:150]}..."  # Replace with IBM Granite call

# Simple KPI forecast
def forecast_kpi(csv_text):
    df = pd.read_csv(StringIO(csv_text))
    df.dropna(inplace=True)
    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]
    model = LinearRegression()
    model.fit(X, y)
    next_year = [[x + 1 for x in X.iloc[-1]]]
    forecast = model.predict(next_year)[0]
    return round(forecast, 2)
