import pandas as pd
import oracledb  # Use oracledb instead of cx_Oracle

# Load cleaned reviews
df = pd.read_csv('../outputs/sentiment_results.csv')

# Connect to Oracle DB
dsn = oracledb.makedsn("localhost", 1521, service_name="XEPDB1")  # Adjust service name if needed
conn = oracledb.connect(user="BANKUSER", password="bankpass123", dsn=dsn)
cursor = conn.cursor()

# Ensure bank names are inserted and map to IDs
bank_ids = {}
for bank in df['bank'].unique():
    cursor.execute("""
        MERGE INTO Banks b 
        USING (SELECT :1 AS name FROM dual) src 
        ON (b.bank_name = src.name) 
        WHEN NOT MATCHED THEN INSERT (bank_name) VALUES (:2)
    """, [bank,bank])
    conn.commit()
    cursor.execute("SELECT bank_id FROM Banks WHERE bank_name = :1", [bank])
    bank_ids[bank] = cursor.fetchone()[0]

# Insert reviews
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO Reviews (review_text, rating, review_date, sentiment, sentiment_score, theme, bank_id)
        VALUES (:1, :2, TO_DATE(:3, 'YYYY-MM-DD'), :4, :5, :6, :7)
    """, (
        row['review'],
        int(row['rating']),
        row['date'],
        row.get('sentiment', None),
        row.get('sentiment_score', None),
        row.get('theme', None),
        bank_ids[row['bank']]
    ))

conn.commit()
cursor.close()
conn.close()

print("✅ Data successfully inserted into Oracle DB.")