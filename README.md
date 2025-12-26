# 🚀 Bitcoin Price Tracker (Day 4)

**Goal:** My first tool that connects to the real internet.

### 🔹 What it does
1.  Connects to the **CoinGecko API**.
2.  Fetches the **Real-Time Bitcoin Price**.
3.  Checks every **30 seconds** automatically.
4.  Uses **Green Text** for success and **Red Text** for errors.

### ⚙️ How to run it
```bash
pip install -r requirements.txt
python day04_api.py


---

# 🪙 Bitcoin ROI Calculator (Day 6)
**Status:** ✅ Deployed
**Type:** CLI Financial Tool

### 🔹 What it does
1.  **Input:** Takes your Bitcoin "Buy Price" from the command line.
2.  **Fetch:** Hits the CoinGecko API for real-time rates.
3.  **Analyze:** Calculates exact Profit/Loss and formats it in USD (e.g., `$34,445.00`).
4.  **Safety:** Handles network crashes and invalid numbers gracefully.

### ⚙️ How to run it
```bash
# Usage: python bitcoin.py [YOUR_BUY_PRICE]
python bitcoin.py 50000