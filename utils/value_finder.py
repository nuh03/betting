def find_value_bets(df, preds, threshold=0.05):
    bets = preds.copy()
    bets["implied_prob"] = 1 / bets["odds1"]
    bets["value"] = bets["model_win_prob"] - bets["implied_prob"]
    value_bets = bets[bets["value"] > threshold]
    return value_bets[["team1", "team2", "model_win_prob", "odds1", "value"]]
