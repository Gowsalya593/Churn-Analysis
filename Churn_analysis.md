/*
===========================================================
📊 CUSTOMER CHURN ANALYSIS - SQL SCRIPT
===========================================================
Database  : powerbi_db
Purpose   : Data Import, Cleaning & Filtering
Author    : Gowsi
===========================================================
*/
-- =========================================================
-- 1️⃣ USE DATABASE
-- =========================================================
USE powerbi_db;

-- =========================================================
-- 2️⃣ VIEW RAW DATA
-- =========================================================
SELECT * FROM customer_data;

-- Count total records
SELECT COUNT(*) AS total_records FROM customer_data;


-- =========================================================
-- 3️⃣ IMPORT DATA FROM CSV (RUN IN CMD / MYSQL CLI)
-- =========================================================

LOAD DATA LOCAL INFILE 'D:/Powerbi/PowerbiTraining.csv'
INTO TABLE customer_data
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

![](/images/count1.jpg)
-- =========================================================
-- 4️⃣ CREATE CLEAN WORKING TABLE
-- =========================================================
CREATE TABLE customer_table AS
SELECT * FROM customer_data;

-- Verify data
SELECT * FROM customer_table;


-- =========================================================
-- 5️⃣ DATA CLEANING - REMOVE NULL CUSTOMER IDs
-- =========================================================
DELETE FROM customer_table
WHERE CustomerID IS NULL;


-- =========================================================
-- 6️⃣ HANDLE MISSING VALUES
-- =========================================================
-- Replace NULL values in TotalCharges with 0
UPDATE customer_table
SET TotalCharges = 0
WHERE TotalCharges IS NULL;


-- =========================================================
-- 7️⃣ BASIC DATA VALIDATION
-- =========================================================
-- Check for remaining NULL values
SELECT COUNT(*) AS null_customer_ids
FROM customer_table
WHERE CustomerID IS NULL;

SELECT COUNT(*) AS null_totalcharges
FROM customer_table
WHERE TotalCharges IS NULL;


-- =========================================================
-- 8️⃣ CREATE FILTERED DATASET FOR ANALYSIS
-- =========================================================
CREATE TABLE filterdata AS
SELECT *
FROM customer_table
WHERE tenure > 3;

-- View filtered data
SELECT * FROM filterdata;


-- =========================================================
-- 9️⃣ ANALYSIS QUERIES (FOR INSIGHTS)
-- =========================================================

-- Total customers
SELECT COUNT(*) AS total_customers FROM filterdata;

-- Churn count
SELECT Churn, COUNT(*) AS count
FROM filterdata
GROUP BY Churn;

-- Average tenure
SELECT AVG(tenure) AS avg_tenure FROM filterdata;

-- Monthly charges analysis
SELECT 
    MIN(MonthlyCharges) AS min_charge,
    MAX(MonthlyCharges) AS max_charge,
    AVG(MonthlyCharges) AS avg_charge
FROM filterdata;

-- Customer distribution by gender
SELECT Gender, COUNT(*) AS total
FROM filterdata
GROUP BY Gender;

-- High-risk churn customers (example logic)
SELECT *
FROM filterdata
WHERE Churn = 'Yes'
AND MonthlyCharges > 70;


-- =========================================================
-- 🔟 FINAL CHECK
-- =========================================================
SELECT COUNT(*) AS final_dataset_count FROM filterdata;

-- =========================================================
-- ✅ END OF SCRIPT
-- =========================================================

