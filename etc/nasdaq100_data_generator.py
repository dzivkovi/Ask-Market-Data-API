"""
This script filters End-of-Day market data for stocks listed in the Nasdaq-100 index.
It consists of approximately 100 of the largest companies listed on the Nasdaq stock exchange.
"""

import pandas as pd

# Placeholder for the list of Nasdaq-100 stock symbols
# Replace this with the actual current list of Nasdaq-100 stocks
nasdaq_100_symbols = [
    'AAPL', 'MSFT', 'AMZN', 'GOOGL', 'GOOG', 'FB', 'TSLA', 'NVDA', 'PYPL', 'INTC',
    'CMCSA', 'PEP', 'CSCO', 'ADBE', 'NFLX', 'COST', 'AVGO', 'TXN', 'CHTR', 'QCOM',
    'AMGN', 'SBUX', 'INTU', 'AMD', 'ISRG', 'BKNG', 'MDLZ', 'GILD', 'FISV', 'VRTX',
    'ATVI', 'ADP', 'CSX', 'REGN', 'LRCX', 'ILMN', 'MU', 'ADSK', 'MELI', 'AMAT',
    'ASML', 'JD', 'BIIB', 'KHC', 'ZM', 'BIDU', 'MAR', 'DOCU', 'DXCM', 'EA',
    'EBAY', 'EXC', 'FAST', 'FIS', 'FOX', 'FOXA', 'IDXX', 'LULU', 'MNST', 'NTES',
    'ORLY', 'PAYX', 'PCAR', 'PDD', 'ROST', 'SIRI', 'SNPS', 'SPLK', 'SWKS', 'TCOM',
    'TMUS', 'VRSK', 'VRSN', 'WBA', 'WDAY', 'XEL', 'XLNX', 'ZM', 'IBM', 'MRNA',
    'TEAM', 'CRWD', 'DDOG', 'OKTA', 'DOCU', 'WDAY', 'CDNS', 'SPLK', 'MTCH', 'ENPH',
    'ETSY', 'ROKU', 'PTON', 'MRVL', 'PANW', 'MPWR', 'MCHP', 'ANSS', 'KLAC', 'CTAS',
    'CDW', 'CPRT', 'DXCM', 'ALGN', 'SGEN', 'ZS', 'TTWO', 'EXPE', 'TCOM', 'ULTA'
]

# Load the data from your CSV file
FILE_PATH = 'path_to_your_file.csv'  # Replace with your End of Day (EOD) stock market data file
data = pd.read_csv(FILE_PATH)

# Filter the data for the Nasdaq-100 symbols
filtered_data = data[data['symbol'].isin(nasdaq_100_symbols)]

# Save the filtered data to a new CSV file
filtered_data.to_csv('nasdaq100_eod_data.csv', index=False)
