import streamlit as st
import yfinance as yf
import plotly.graph_objects as go




stock = st.text_input("Stock", autocomplete=None)
if len(stock):
    dat = yf.Ticker(stock)
    his = dat.history(period='1mo')

    st.write(stock.upper()+ " Graph:")
    fig = go.Figure(data=[go.Candlestick(x=his.index,
                open=his["Open"],
                high=his["High"],
                low=his["Low"],
                close=his["Close"])])

    st.plotly_chart(fig)

    st.write(stock.upper() + " data:")
    st.write(his)

    