# MacroPulse

MacroPulse is a Python-based macroeconomic monitoring project that uses the FRED API to track key U.S. economic indicators and generate a composite macroeconomic strength score.

The project currently analyzes:
- Unemployment rate
- Inflation
- Federal Funds Rate

and combines them into a single:

## MacroPulse Score (0–100)

The goal of the project is to create a simple and interpretable macroeconomic "health index" using publicly available economic data.

---

# Features

- Fetches live economic data from the FRED API
- Calculates inflation using CPI data
- Generates a weighted macroeconomic score
- Assigns economic environment classifications
- Displays a clean macro dashboard visualization
- Modular Python project structure

---

# Project Structure

```text
macropulse/
├── notebooks/
│   └── dashboard.ipynb
├── src/
│   ├── fred_client.py
│   ├── indicators.py
│   └── scoring.py
├── README.md
└── .gitignore
```

---

# Technologies Used

- Python
- pandas
- matplotlib
- fredapi
- Jupyter Notebook

---

# Example Output

- MacroPulse Score: 74.2 / 100
- Environment: Stable Expansion

The score is calculated using weighted economic indicators:
- Labor market conditions
- Inflation stability
- Interest rate environment

---

# Future Improvements

- Additional economic indicators
- Historical backtesting
- Interactive dashboard
- Recession probability modeling
- Automated report generation

---

# Data Source

Federal Reserve Economic Data (FRED):
https://fred.stlouisfed.org/

---

# Author

Anthony Sardina