import streamlit as st
import pandas as pd
from model.trainer import train_model
from model.predictor import predict
from utils.value_finder import find_value_bets
from data.fetch_matches import load_matches

st.set_page_config(page_title="Voetbal AI", layout="wide")
st.title("⚽ Voetbal AI Value Betting Tool")

df = load_matches()
model = train_model(df)

st.subheader("Actuele Wedstrijden")
matches = df[["team1", "team2", "spi1", "spi2", "prob1", "prob2", "probtie", "odds1", "odds2", "oddsx"]]

preds = predict(model, df)
value_bets = find_value_bets(df, preds)

st.dataframe(value_bets)
