CREATE TABLE IF NOT EXISTS thing (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    reddit_id TEXT,
    type TEXT,
    created_utc INTEGER
);

CREATE TABLE IF NOT EXISTS data (
    thing_id INTEGER NOT NULL,
    key TEXT NOT NULL,
    value BLOB NOT NULL,
    retrieved_on INTEGER
);