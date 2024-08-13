import pandas as pd

def calculate_investment_plan(savings, monthly, horizon, thesauration, total_savings, expected_return_rate_in_percent, inflation_rate):
    total = 0
    returns = 0
    aggregated_returns = 0
    received_returns = 0 
    rows = [
        {
            "Year": 0,
            "Value": total_savings,
            "YearlyReturns": 0,
            "AggregatedReturns": 0,
            "ReceivedReturns": 0,
            "Total": total_savings,
            "Net Total": total_savings,
            "NetYearlyReturns": 0
        }
    ]
    for i in range(1, horizon + 1):
        if monthly:
            yearly_savings = savings * 12
        else:
            yearly_savings = savings
        total_savings += yearly_savings
        
        # Determines whether returns will be added to savings or "paid"
        if thesauration:
            total_savings = total_savings * (1 + (expected_return_rate_in_percent/100))
        else:
            received_returns += (expected_return_rate_in_percent/100) * total_savings
        
        aggregated_returns += (expected_return_rate_in_percent/100) * total_savings
        yearly_returns = (expected_return_rate_in_percent/100) * total_savings
        total = total_savings + received_returns
        net_worth = total / (1 + (inflation_rate/100))**i
        net_yearly_returns = yearly_returns / (1 + (inflation_rate/100))**i
        row = {
            "Year": i,
            "Value": round(total_savings, 2),
            "YearlyReturns": round(yearly_returns, 2),
            "AggregatedReturns": round(aggregated_returns, 2),
            "ReceivedReturns": round(received_returns, 2),
            "Total": round(total, 2),
            "Net Total": round(net_worth, 2),
            "NetYearlyReturns": round(net_yearly_returns, 2)
        }
        rows.append(row)
    return pd.DataFrame(rows)