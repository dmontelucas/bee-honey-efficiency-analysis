import statsmodels.api as sm

def run_regression(df):
    X = df[["pollen_input_g", "temperature", "humidity"]]
    y = df[["honey_output_g"]]
    X = sm.add_constant(X)
    model = sm.OLS(y, X).fit()
    return model