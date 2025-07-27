import pandas as pd

def load_matches():
    url = "https://projects.fivethirtyeight.com/soccer-api/club/spi_matches_latest.csv"
    df = pd.read_csv(url)
    df = df[df["league"].notna()]
    return df
