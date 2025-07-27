import pandas as pd

def predict(model, df):
    X = df[["spi1", "spi2", "prob1", "prob2", "probtie"]]
    probs = model.predict_proba(X)
    df["model_win_prob"] = probs[:, 1]
    return df
