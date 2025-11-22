📊 Simple ETL Pipeline (Python + SQLite)

A clean and beginner-friendly ETL (Extract-Transform-Load) pipeline built using Python, Pandas, and SQLite.
The pipeline reads raw transaction data from a CSV file, transforms it, loads it into a SQLite database, and logs each step.

🚀 Features

Extract data from CSV

Transform data (cleaning + add computed fields)

Load clean data into SQLite database

Automatic Logging stored in /logs/pipeline.log

Modular code (extract.py, transform.py, load.py, run_pipeline.py)

100% portable — no Docker, no Airflow required

📁 Project Structure
simple-etl-pipeline
│   .gitignore
│   README.md
│
├── data
│   └── transactions.csv
│
├── database
│   └── etl.db
│
├── etl
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── run_pipeline.py
│
└── logs
    └── pipeline.log

🧩 How the ETL Works
1️⃣ Extract

Loads CSV file into a Pandas DataFrame.

2️⃣ Transform

Cleans data

Ensures amount is numeric

Adds a new field:

amount_with_tax = amount * 1.07

3️⃣ Load

Inserts the transformed data into a SQLite database table called transactions.

▶️ Run the Pipeline

From inside the etl folder:

python run_pipeline.py


Check logs:

cat ../logs/pipeline.log


Verify database contents:

import sqlite3
conn = sqlite3.connect("../database/etl.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM transactions;")
print(cursor.fetchall())

📌 Example Database Output
(1, 'Alice', 120.5, 128.935)
(2, 'Bob', 75.2, 80.464)
(3, 'Charlie', 200.0, 214.0)
(4, 'David', 50.0, 53.5)
(5, 'Eve', 340.8, 364.656)
