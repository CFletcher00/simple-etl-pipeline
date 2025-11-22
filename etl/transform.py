def transform(df):
    df["amount"] = df["amount"].astype(float)
    df["amount_with_tax"] = df["amount"] * 1.07
    return df
