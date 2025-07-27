import pandas as pd

def load_matches():
    df = pd.read_csv("data/spi_matches.csv")
    df = df[df["league"].notna()]
    return df
