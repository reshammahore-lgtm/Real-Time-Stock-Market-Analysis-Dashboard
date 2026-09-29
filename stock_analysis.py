import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("stock_data.csv", parse_dates=["Date"])

# 20-day moving average
df["MA20"] = df["Close"].rolling(20).mean()

# 14-day RSI
delta = df["Close"].diff()
gain = delta.clip(lower=0).rolling(14).mean()
loss = (-delta.clip(upper=0)).rolling(14).mean()
rs = gain / loss.replace(0, pd.NA)
df["RSI14"] = 100 - (100 / (1 + rs))

print(df[["Date", "Close", "MA20", "RSI14", "Volume"]].tail(10))

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(df["Date"], df["Close"], label="Close Price")
ax.plot(df["Date"], df["MA20"], label="20-Day MA")
ax.set_title("Stock Price and 20-Day Moving Average")
ax.set_xlabel("Date")
ax.set_ylabel("Price")
ax.legend()
plt.tight_layout()
plt.savefig("price_moving_average.png", dpi=150)
plt.show()

plt.figure(figsize=(10, 4))
plt.plot(df["Date"], df["RSI14"], label="RSI (14)")
plt.axhline(70, linestyle="--", label="Overbought 70")
plt.axhline(30, linestyle="--", label="Oversold 30")
plt.title("Relative Strength Index")
plt.xlabel("Date")
plt.ylabel("RSI")
plt.legend()
plt.tight_layout()
plt.savefig("rsi.png", dpi=150)
plt.show()
