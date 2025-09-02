# automated-financial-analyzer

# Automated Financial Analysis Platform



A full-stack application that automates the process of fetching financial data for companies, applies a rule-based engine to generate investment insights (pros & cons), and presents them through a dynamic web dashboard.

## Key Features

* **Automated Data Pipeline**: A Python script fetches key financial metrics for a predefined list of companies from a REST API.
* **Rule-Based Analysis Engine**: Analyzes metrics like Debt-to-Equity, Return on Equity (ROE), and profit growth to generate qualitative pros and cons for each stock.
* **Dynamic Web Dashboard**: A Flask application displays a list of all analyzed companies and provides dedicated pages for detailed insights on each one.
* **Persistent Data Storage**: Leverages a MySQL database with SQLAlchemy to store and manage analysis results, including company info, logos, and financial metrics.

## Demo Video
https://drive.google.com/file/d/1tZjym8gRo_lxcMUyL8EJP_PnR90_K9n7/view?usp=sharing




## Tech Stack

* **Backend**: Python, Flask
* **Data Processing**: Pandas, Requests
* **Database ORM**: SQLAlchemy, Flask-SQLAlchemy
* **Database**: MySQL
* **Frontend**: HTML,CSS


## Project Structure

```
/automated-financial-analyzer
|
|-- ML Financial Analysis Project.py
|-- app.py
|-- requirements.txt
|-- company_id.xlsx
|-- README.md
|
└─── templates/
     |-- company_list.html
     |-- company_detail.html
```

## Setup and Installation

Follow these steps to set up and run the project locally.

### 1. Prerequisites

* Python 3.10+
* A running MySQL server

### 2. Clone the Repository

```bash
git clone [https://github.com/YourUsername/automated-financial-analyzer.git](https://github.com/YourUsername/automated-financial-analyzer.git)
cd automated-financial-analyzer
```

### 3. Set Up a Virtual Environment

```bash
# Create the virtual environment
python -m venv venv

# Activate it (Linux/macOS)
source venv/bin/activate

# Activate it (Windows)
.\venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a file named `.env` in the root of the project directory. This file will hold your secret keys and database connection details.

```
API_KEY="your_api_key_from_bluemutualfund"
MYSQL_USER="your_mysql_username"
MYSQL_PASSWORD="your_mysql_password"
MYSQL_HOST="localhost"
MYSQL_DB="ml_finance"
```

### 6. Set Up the MySQL Database

Connect to your MySQL server and run the following SQL script to create the database and the required table. The table schema is based on the Flask model in `app.py`.

```sql
-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS ml_finance;

-- Use the newly created database
USE ml_finance;

-- Create the table to store analysis results
CREATE TABLE ml_results (
    company_id VARCHAR(32) PRIMARY KEY,
    company_name VARCHAR(255),
    logo_url VARCHAR(512),
    website VARCHAR(512),
    pros TEXT,
    cons TEXT,
    roe_3y FLOAT,
    debt_equity FLOAT,
    div_payout FLOAT,
    profit_growth_5y FLOAT,
    sales_growth_10y FLOAT
);
```

## How to Run the Application

### Step 1: Run the Data Ingestion Script

Execute the `ML Financial Analysis Project.py` script. This will fetch data from the API, analyze it, and populate your MySQL database.

```bash
python ML Financial Analysis Project.py
```

### Step 2: Run the Flask Web Application

Once the database is populated, start the Flask server.

```bash
flask run
```

The application will be available at `http://127.0.0.1:5000`. This will automatically redirect you to the `/companies` page.

## License

This project is licensed under the MIT License.
