-- Connect as BANKUSER
-- Table: Banks
CREATE TABLE Banks (
    bank_id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    bank_name VARCHAR2(100) UNIQUE NOT NULL
);

-- Table: Reviews
CREATE TABLE Reviews (
    review_id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    review_text CLOB NOT NULL,
    rating NUMBER NOT NULL,
    review_date DATE NOT NULL,
    sentiment VARCHAR2(20),
    sentiment_score FLOAT,
    theme VARCHAR2(50),
    bank_id NUMBER NOT NULL,
    FOREIGN KEY (bank_id) REFERENCES Banks(bank_id)
);
