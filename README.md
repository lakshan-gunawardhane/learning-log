# 👨‍💻 Lakshan's Learning Log (2025)

**Goal:** Become a Chief AI Architect ($1,000/hr) by 2030.
---
**Quick Links:**
[💼 Day 7: Crypto Portfolio](#-day-7-bonus-crypto-portfolio-manager) • [🛡️ Day 7: Web Sentinel](#-day-7-web-sentinel) • [💱 Day 6: Currency Converter](#-day-6-global-currency-converter)
---
---


## 💼 Day 7 (Bonus): Crypto Portfolio Manager
**Status:** ✅ Deployed | **Tech:** Python, API, Sys, Math

A CLI financial tool that calculates real-time Net Worth of crypto assets.
* **Smart Input:** Reads pairs of data (Coin + Amount) directly from the terminal.
* **Logic:** Uses `range(start, stop, step)` to process inputs in pairs.
* **Live Data:** Fetches real-time prices via the CoinGecko API.

**Usage:**
```bash
python day07_portfolio.py bitcoin 0.5 ethereum 10
```

## 🛡️ Day 7: Web Sentinel
**Status:** ✅ Deployed | **Tech:** Python, Sys, Requests

A CLI tool that monitors the health of websites. It takes multiple URLs as arguments and reports if they are Online (200 OK) or Down.

* **Usage:** `python day07_sentinel.py google.com my-broken-site.com`
* **Features:** Auto-adds `https://`, handles timeouts, and reports status codes.


----

## 💱 Day 6: Global Currency Converter
**Status:** ✅ Deployed | **Tech:** Python, API, Math

A universal converter that uses a "Cross-Rate" formula to swap between any two world currencies.
* **Smart Math:** Calculates `(Amount / From_Rate) * To_Rate` to bridge currencies.
* **Safety:** Auto-detects network failures and prevents crashes.
* **User-Friendly:** Loops until valid currency codes are entered.

**Usage:**
```bash
python day06_converter.py

```
----

## 🪙 Day 6: Bitcoin ROI Calculator
**Status:** ✅ Deployed

A tool that checks real-time Bitcoin prices to calculate profit.
* **Usage:** `python bitcoin.py 50000`

---

## 🚀 Day 4: Bitcoin Price Tracker
**Status:** ✅ Deployed

My first API tool that tracks prices automatically.
* **Usage:** `python day04_api.py`

---

## 🛠️ Installation
1. `git clone https://github.com/lakshan-gunawardhane/learning-log.git`
2. `pip install requests`