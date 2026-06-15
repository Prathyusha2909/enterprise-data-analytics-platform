# Power BI Dashboard Guidance

This document describes how to use Power BI with the Enterprise Data Analytics Platform.

## Recommended visuals

- Revenue trend line chart
- Transaction volume bar chart by date or business unit
- Customer retention and repeat purchase metrics
- KPI cards for total revenue, total transactions, and average order value
- Category or business unit performance matrix

## Data sources

- Connect Power BI Desktop to PostgreSQL using the database connection string.
- Use the `transactions` table as the primary fact table.
- Optionally create calculated measures for retention, revenue growth, and customer lifetime value.

## Dashboard tips

- Use date filters or slicers to support ad hoc time period analysis.
- Surface top customers and top categories through dynamic table visuals.
- Add a Power BI report page for business performance overview and another for operational detail.
