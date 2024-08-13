import streamlit as st
from helpers import calculate_investment_plan

# Streamlit app details
st.set_page_config(page_title="Investment Analysis", layout="wide")
with st.sidebar:
    st.title("Investment Analysis")
    savings = st.number_input("Yearly or monthly saving amount", value=12000)
    monthly = st.selectbox("Period", ["Yearly", "Monthly"])
    thesauration = st.toggle("Thesauration", value=True)
    horizon = st.number_input("Horizon", value=10, step=1)
    total_savings = st.number_input("Current Savings", value = 20000)
    expected_return_rate_in_percent = st.number_input("Expected Return Rate in %", value=5)
    inflation_rate = st.number_input("Infation Rate", value=2)
    # period = st.selectbox("Enter a time frame", ("1D", "5D", "1M", "6M", "YTD", "1Y", "5Y"), index=2)
    button = st.button("Submit")

# Format market cap and enterprise value into something readable


# If Submit button is clicked
if button:
    
    if monthly == "Monthly":
        monthly = True
    else:
        monthly = False

    st.write(
        calculate_investment_plan(
            savings,
            monthly,
            horizon,
            thesauration,
            total_savings,
            expected_return_rate_in_percent,
            inflation_rate
        )
    )

