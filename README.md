# Real-Time Stock Market Analysis Dashboard

A portfolio project demonstrating stock-market data analysis with Python and a Power BI-ready dataset.

## Features
- Stock price and trading-volume analysis
- 20-day Moving Average
- 14-day Relative Strength Index (RSI)
- Trend and volatility-oriented visualizations
- CSV dataset structured for Power BI import

## Technologies
- Python
- Pandas
- NumPy
- Matplotlib
- Microsoft Power BI

## Files
- `stock_data.csv` — sample market dataset and calculated indicators
- `stock_analysis.py` — Python analysis and chart generation
- `price_moving_average.png` — price/MA preview
- `rsi.png` — RSI preview

## Power BI
Import `stock_data.csv` into Power BI and create:
1. Line chart: Date vs Close and MA20
2. Line chart: Date vs RSI14
3. Column chart: Date vs Volume
4. Cards: latest Close, latest Volume, latest RSI14
5. Slicers: Date

## Note
This repository is a portfolio prototype using a sample dataset. A production real-time dashboard would connect Power BI/Python to a live market-data API and refresh the data automatically.
