import streamlit as st
import yfinance as yf

# Streamlit code
st.title("Stock Fundamental Data")

# Get the stock symbol from the user
symbol = st.text_input("Enter the stock symbol (format - SYMBOL.NS for NSE and SYMBOL.BO for BSE): ")

if symbol:
    try:
        # Fetch stock data using yfinance
        stock = yf.Ticker(symbol)

        # Get fundamental data
        info = stock.info

        # Display fundamental data in a table
        st.write("## Fundamental Data for", symbol)
        st.write("```")
        for key, value in info.items():
            # Capitalize the first letter of the key
            key_formatted = key.capitalize()
            st.write(f"{key_formatted}: {value}")
        st.write("```")
    except Exception as e:
        st.error(f"Error: {e}")