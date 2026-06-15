# Power BI Dashboard Assets

This folder is reserved for Power BI reports and dataset files related to the Enterprise Data Analytics Platform.

Recommended contents:

- `.pbix` dashboard files
- Data model notes
- Report usage documentation
- `dashboard-guidance.md` for Power BI visualization and reporting best practices

## Dashboard Template

The `dashboard.svg` file provides a visual preview of the KPI dashboard layout showing key metrics: Total Revenue, Transactions, Customer Retention, and Revenue Growth trends. Use this as reference when building your Power BI reports.

## Power BI Workflow

1. Open Power BI Desktop.
2. Connect to the PostgreSQL database using the analytics connection string.
3. Import the `transactions` table as the primary data source.
4. Build report pages for revenue, transaction volume, customer retention, and operational metrics.
5. Create measures for revenue growth, average order value, and retention.
6. Save the report file to this folder once finished.
