import pandas as pd

CLEAN_PATH = "../data/cleaned/superstore_cleaned_python.csv"

def load_clean_data(path):
    df = pd.read_csv(path, parse_dates=["Order Date", "Ship Date"])
    return df

def run_checks(df):
    results = []

    # 1. No missing values in required columns
    required_cols = ["Order ID", "Order Date", "Sales", "pProfit", "Quantity"]
    missing = df[required_cols].isnull().sum().sum()
    results.append(("No missing values in required columns", missing == 0, missing))

    # 2. No exact duplicate rows
    exact_dupes = df.duplicated().sum()
    results.append(("No exact duplicate rows", exact_dupes == 0, exact_dupes))

    # 3. No true Order ID + Product ID duplicates
    #
    #
    full_dupes = df.duplicated(
        subset=["Order ID", "Product ID", "Sales", "Quantity", "Discount", "Profit"]
    ).sum()
    results.append(("No true Order+Product+values duplicates", full_dupes == 0, full_dupes))

    # 4. Discount values within valid range (0-1)
    invalid_discount = ((df["Discount"] < 0) | (df["Discount"] > 1)).sum()
    results.append(("Discount values within 0-1 range", invalid_discount == 0, invalid_discount))

    # 5. No negative Sales
    negative_sales = (df["Sales"] < 0).sum()
    results.append(("No negative Sales values", negative_sales == 0, negative_sales))

    # 6. Ship Date never before Order Date
    ship_before_order = (df["Ship Date"] < df["Order Date"]).sum()
    results.append(("Ship Date never before Order Date", ship_before_order == 0, ship_before_order))

    # 7. No failed date parses
    failed_dates = df["Order Date"].isnull().sum()
    results.append(("All Order Date values parsed correctly", failed_dates == 0, failed_dates))

    # 8. Quantity alway positive
    invalid_qty =(df["Quantity"] <= 0).sum()
    results.append(("Quantity always positive", invalid_qty == 0, invalid_qty))

    return results

# 
def print_summary(results):
    passe = 0
    print("=" * 60)
    print("DATA VALIDATION RESULTS")
    print("=" * 60)
    for name, ok, detail in results:
        status = "PASS" if ok else "FAIL"
        symbol = "\u2713" if ok else "\2717"
        print(f"{symbol} [{status}] {name}" + ("" if ok else f" (found: {detail})"))
        if ok:
            passed += 1
    print("=" * 60)
    print(f"{passed}/{len(results)} checks passed")
    print("=" * 60)

    def main():
        df = load_clean_data(CLEAN_PATH)
        results = run_checks(df)
        print_summary(results)

    if __name__ == "__main__":
        main()

    