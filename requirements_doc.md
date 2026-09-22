# Requirements Document — Retail Business Performance Dashboard

Simulated stakeholder request, written as if a business user had approached the analytics function with a reporting need. This document defines the scope the dashboard was built to satisfy.

## Requesting Stakeholder (Simulated)

Regional Sales Manager, Retail Division

## Business Need

"I need a way to see how our sales and profit are performing across regions and product categories without waiting on a manual report each month. I also want to understand whether our discounting is actually hurting our margins, and if so, where."

## Objectives

1. Provide a single view of overall business performance (sales, profit, orders, margin) that updates as new data comes in.
2. Allow drill-down from company-wide totals to individual products and sub-categories.
3. Identify whether discount levels are correlated with reduced profitability, and flag any specific product lines at risk.
4. Support ad hoc questions without requiring a new report to be built from scratch each time.

## Scope

**In scope**
- Sales, profit, discount, and order-level data for the reporting period (2014-2017, per the source dataset)
- Region, category, sub-category, and product-level breakdowns
- One dedicated page answering the discount-and-profitability question directly

**Out of scope**
- Real-time/live data refresh (source data is static for this project)
- Customer-level marketing or CRM data
- Inventory or supply chain data
- Forecasting or predictive modeling (descriptive/diagnostic analysis only)

## Deliverables

1. A 3-page Power BI dashboard:
   - Executive Summary (top-line KPIs and trends)
   - Product Analysis (drill-down by category, sub-category, and product)
   - Ad Hoc Analysis (direct answer to the discounting question)
2. A written insights memo summarizing key findings and recommendations
3. A written ad hoc analysis response addressing the discounting question specifically
4. Supporting documentation: data dictionary, cleaning process, and data quality notes

## Success Criteria

- Stakeholder can identify top and bottom performing regions/categories without needing to ask an analyst
- Stakeholder has a clear, data-backed answer to whether discounting is hurting profit, and which sub-categories are affected
- All figures in the dashboard are traceable back to a documented, validated data source