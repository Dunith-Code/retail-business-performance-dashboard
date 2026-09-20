import pandas as pd

# load the raw data
RAW_PATH = r"D:\Z\my-projects\data-science\retail-business-performance-dashboard\data\raw\superstore.csv"

CLEAN_PATH = r"D:\Z\my-projects\data-science\retail-business-performance-dashboard\data\cleaned\superstore_cleaned_python.csv"
 
def load_data(path):
    # load csv
    df = pd.read_csv(path, encoding="latin1")
    print(f"Loaded {df.shape[0]} rows, {df.shape[1]} columns")
    return df

def inspect_data(df):
    # inspect data
    print(df.head())
    print(df.info())
    print(df.describe())

def check_nulls(df):
    # check null values
    nulls = df.isnull().sum()
    pct = (nulls / len(df)) * 100
    print("Nulls per column:\n", nulls)
    print("Nulls (%):\n", pct)
    return nulls

# check and resolve duplicates
def check_and_resolve_duplicates(df):

    exact_dupes = df.duplicated().sum()
    print("Exact duplicate rows:", exact_dupes)

    dup_check = df.duplicated(subset=["Order ID", "Product ID"], keep=False)
    print("Order ID + Product ID marches:", dup_check.sum())

    before = len(df)
    df = df.drop_duplicates(
        subset=["Order ID", "Product ID", "Sales", "Quantity", "Discount", "Profit"],
        keep="first",
    )
    after = len(df)
    print(f"Removed {before - after} true duplicate row(s)")
    return df

# convert dates
def convert_dates(df):
    df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
    df["Ship Date"] = pd.to_datetime(df["Ship Date"], errors="coerce")

    failed = df["Order Date"].isnull().sum()
    print("Failed Order Date conversions:", failed)
    if failed:
        print(df[df["Order Date"].isnull()][["Row ID", "Order ID", "Order Date"]])
    return df

# run sanity checks
def run_sanity_checks(df):
    negative_sales = (df["Sales"] < 0).sum()
    invalid_discount = ((df["Discount"] < 0) | (df["Discount"] > 1)).sum()
    ship_before_order = df[df["Ship Date"] < df["Order Date"]]

    print("Negative Sales rows:", negative_sales)
    print("Invalid discount values:", invalid_discount)
    print("Ship-before-order issues:", len(ship_before_order))

# 
def add_calculated_columns(df):
    df["Profit Margin"] = df["Profit"] / df["Sales"]
    df["Order Year"] = df["Order Date"].dt.year
    df["Order Month"] = df["Order Date"].dt.month
    df["Shipping Days"] = (df["Ship Date"] - df["Order Date"]).dt.days

    # 
    def band(discount):
        if discount == 0:
            return "No Discount"
        elif discount <= 0.2:
            return "Low (1-20%)"
        elif discount <= 0.4:
            return "Medium (21-40%)"
        else:
            return "High (40%+)"

    df["Discount Band"] =  df["Discount"].apply(band)

    # 
    df["Postal Code"] = df["Postal Code"].astype(str)

    return df

# 
def save_data(df, path):
    df.to_csv(path, index=False)
    print(f"Saved Cleaned file: {len(df)} rows -> {path}")

# 
def main():
    df = load_data(RAW_PATH)
    inspect_data(df)
    check_nulls(df)
    df = check_and_resolve_duplicates(df)
    df = convert_dates(df)
    run_sanity_checks(df)
    df = add_calculated_columns(df)
    save_data(df, CLEAN_PATH)

# 
if __name__ == "__main__":
    main()
