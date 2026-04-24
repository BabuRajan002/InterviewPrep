import re 
from pathlib import Path 
import sys
from collections import defaultdict 

LOG_PATTERN = re.compile(
    r'(?P<date>\d{4}-\d{2}-\d{2})\s(?P<time>\d{2}:\d{2}:\d{2})\s*\|\s*(?P<ticker>\w+)\s*\|\s*(?P<action>BUY|SELL)\s*\|\s*(?P<price>[\d.]+)+\s*\|\s*(?P<quantity>\d+)'
)

def metric_aggregator(path: str):
    filePath = Path(path)

    try: 
        with open(filePath, 'r') as f:
            for line in f:
                line = line.strip()

                if not line:
                    continue

                match = LOG_PATTERN.search(line)

                if match:
                    yield {
                        "ticker" : match.group("ticker"),
                        "price" : match.group("price"),
                        "quantity" : match.group("quantity")
                    }
                else:
                    print(f"Found a Malformed Line: {line}")
    except FileNotFoundError:
        print(f"Error due to {filePath} not found", file=sys.stderr)

if __name__ == "__main__":
    logPath = "/Users/babus/Desktop/repos/InterviewPrep/Python/SREInterviewPrep/Nasdaq/trades.log"

    total = defaultdict(int)
    total_price = 0
    count = 0.0

    for data in metric_aggregator(logPath):
        ticker = data['ticker']
        quantity = int(data['quantity'])
        price = float(data['price'])
        total[ticker] += quantity
        if data['ticker'] == 'AAPL':
            total_price += price
            count += 1
        avgPrice = total_price / count if count > 0 else 0 

    print(f"\n total volumes traded")
    for ticker, volume in total.items():
        print(f"{ticker:<10} : {volume:<12}")
    print(f"\n Average price for AAPL is: {avgPrice:.2f}")
    




