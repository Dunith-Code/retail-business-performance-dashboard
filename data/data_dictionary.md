# Data Dictionary - Retail Business Performance Dashboard

## Source
- Dataset: Superstore Sales Dataset (Kaggle)
- Rows: 9,994 raw → 9,993 after cleaning
- Columns: 21 raw → 26 after calculated fields added
- Time range: 2014 - 2017

## Columns
| Column | Type | Description |
|---|---|---|
| Row ID | Integer | Row-level identifier from the source file |
| Order ID | Text | Order identifier (shared across all line items in one order) |
| Order Date | Date | Date the order was placed |
| Ship Date	| Date | Date the order was shipped |
| Ship Mode |	Text | Shipping method (e.g. Standard Class, Second Class) |
| Customer ID |	Text | Unique customer identifier |
| Customer Name |	Text |	Customer's full name |
| Segment |	Text |	Customer segment (Consumer, Corporate, Home Office) |
| Country |	Text	| Country of the order |
| City |	Text	| City of the order |
| State	| Text |	State of the order |
| Postal Code |	Text |	ZIP/postal code (converted from integer during cleaning - see below) |
| Region	| Text |	Sales region (West, East, Central, South) |
| Product ID	| Text |	Unique product identifier |
| Category |	Text	| Top-level product category |
| Sub-Category |	Text |	Product sub-category |
| Product Name |	Text |	Full product name |
| Sales | Decimal | Revenue for the line item |
| Quantity |	Integer |	Units ordered |
| Discount |	Decimal |	Discount rate applied to the line item (0–1) |
| Profit	| Decimal	| Profit for the line item (can be negative) |
|||

## Calculated Fields
- This formulas added for cleaning data.

| Field	| Formula / Logic	| Purpose |
| --- | --- | --- |
| Profit Margin	| Profit / Sales |	Line-item profitability ratio |
| Order Year	| Extracted from Order Date |	Time-based grouping/filtering |
| Order Month	| Extracted from Order Date |	Time-based grouping/filtering |
| Shipping Days	| Ship Date - Order Date |	Delivery time analysis |
| Discount Band |	No Discount / Low (1–20%) / Medium (21–40%) / High (40%+)	| Groups line items for discount-vs-profit analysis (Ad Hoc Analysis page) |
|||

- `Discount Band` is also implemented as a DAX calculated column directly in Power BI. The Python-generated version is retained in the cleaned CSV for documentation and EDA purposes but excluded from the Power BI model to avoid a duplicate field, the DAX version is the one the dashboard uses

## Data Quality Checks Performed

| Check	| Result |
| --- | --- |
| Missing values (all columns) |	0 - no nulls found anywhere in the raw file |
| Exact duplicate rows |	0 |
| Order ID + Product ID matches	| 16 found - investigated individually |
| Failed date parses (Order Date) |	0 |
| Negative Sales values	| 0 |
| Invalid Discount values (outside 0 - 1)	| 0 |
| Ship Date before Order Date	| 0 |
|||

## Duplicate Investigation — Detail
16 rows shared the same Order ID + Product ID combination. Each was inspected manually rather than dropped automatically, since a repeated Order ID + Product ID pair can legitimately represent two separate order lines (e.g. the same product added to an order at different quantities or discount levels).

- 15 pairs had differing Quantity, Sales, and/or Discount values — confirmed as legitimate separate order lines, kept as-is.
- 1 pair (Order `US-2014-150119`, Product `FUR-CH-10002965`, Row IDs 3406 and 3407) matched on every column except Row ID - confirmed as a true duplicate and removed, keeping the first occurrence.

Final row count after removal: 9,993.

## Data Type Corrections
- `Order Date` and `Ship Date` - loaded as text, converted to proper Date type
- `Postal Code` - loaded as an integer; converted to text/string, since postal codes are identifiers, not quantities, and should never be summed or averaged

## Limitations
- Dataset covers 2014–2017 only; it does not reflect current business performance and is used here purely as a stand-in dataset for demonstrating the analytics workflow.
- `Discount Band` thresholds (20% / 40% cutoffs) were chosen as reasonable round-number bands for this analysis; a real business would define these based on actual margin-tolerance policy rather than analyst judgment.