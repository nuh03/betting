from sklearn.linear_model import LogisticRegression

def train_model(df):
    from sklearn.model_selection import train_test_split
    df = df.dropna(subset=["score1", "score2"])
    df["result"] = (df["score1"] > df["score2"]).astype(int)
    X = df[["spi1", "spi2", "prob1", "prob2", "probtie"]]
    y = df["result"]
    model = LogisticRegression()
    model.fit(X, y)
    return model
