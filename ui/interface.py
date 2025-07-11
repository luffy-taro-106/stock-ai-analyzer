
from rich.console import Console
from fetch.fetch_data import fetch_stock_data
from analysis.patterns import dummy_pattern_detection
from db.sqlite_handler import store_to_db
from insights.ai_insight import generate_insight

def run_cli():
    console = Console()
    ticker = input("Enter stock ticker: ")
    df = fetch_stock_data(ticker)
    store_to_db(df)
    signal_df = dummy_pattern_detection(df)
    context = str(signal_df.head(3))
    insight = generate_insight(context)
    console.print(f"[bold magenta]Insight:[/bold magenta] {insight}")

