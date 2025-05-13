CREATE TABLE stores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    latitude REAL NOT NULL,
    longitude REAL NOT NULL,
    cashless_payment TEXT NOT NULL,  -- '対応', '一部対応', '未対応' など
    address TEXT,
    phone_number TEXT,
    opening_hours TEXT
);
