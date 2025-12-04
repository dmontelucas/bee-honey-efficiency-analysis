def calculate_efficiency(df):
    df["efficiency"] = df ["honey_output_g"] / df["pollen_input_g"]
    df["honey_per_hour"] = df ["honey_output_g"] / df["time_hours"]
    return df