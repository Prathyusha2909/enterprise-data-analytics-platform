CREATE TABLE IF NOT EXISTS transactions (
    transaction_id TEXT PRIMARY KEY,
    transaction_date TIMESTAMP NOT NULL,
    customer_id TEXT NOT NULL,
    amount NUMERIC(12, 2) NOT NULL,
    product_category TEXT,
    business_unit TEXT,
    status TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_transactions_customer_id ON transactions(customer_id);
CREATE INDEX IF NOT EXISTS idx_transactions_transaction_date ON transactions(transaction_date);
