import pathlib

DB_FOLDER = "SQLiteDataBase" 
DB_FILE = "exchange.db"
JSON_FOLDER = "JSON"
JSON_RATES_FILE = "exchange_2022_02_11.json"
JSON_COUNTRIES_FILE = "country_code_and_details.json"
CSV_FOLDER = "SCV"
TABLE_RATES = "rates"
TABLE_COUNTRIES = "countries"
TABLE_CONVERSIONS_HISTORY = "conversions"
PATH_TO_DB = pathlib.Path(__file__).parent.joinpath(DB_FOLDER, DB_FILE)
PATH_TO_JSON = pathlib.Path(__file__).parent.joinpath(JSON_FOLDER)
PATH_TO_RATES_JSON = pathlib.Path(__file__).parent.joinpath(JSON_FOLDER, JSON_RATES_FILE)
PATH_TO_COUNTRIES_JSON = pathlib.Path(__file__).parent.joinpath(JSON_FOLDER, JSON_COUNTRIES_FILE)

SQL_CREATE_TABLE_RATES = F"""
    CREATE TABLE IF NOT EXISTS "{TABLE_RATES}" (
        "code"	TEXT NOT NULL UNIQUE,
        "rate_to_euro" REAL,
        "date"	TEXT,
        PRIMARY KEY("code")
    );
""" 

SQL_CREATE_TABLE_COUNTRIES = F"""
    CREATE TABLE IF NOT EXISTS "{TABLE_COUNTRIES}" (
        "country_code"	TEXT NOT NULL UNIQUE,
        "continent_name" TEXT,
        "country_name" TEXT,
        "continent_code" TEXT,
        "capital_name" TEXT,
        "currency_code"	TEXT,
        "phone_code"	TEXT,
        "three_letter_country_code"	TEXT,
        PRIMARY KEY("country_code"),
        FOREIGN KEY("currency_code") REFERENCES "rates"("code")
    );
""" 

SQL_CREATE_TABLE_CONVERSIONS = F"""
    CREATE TABLE IF NOT EXISTS "{TABLE_CONVERSIONS_HISTORY}" (
        "id" NUMBER AUTO INCREMENT PRIMARY KEY NOT NULL UNIQUE,
        "from_currency_code" TEXT,
        "to_currency_code" TEXT,
        "amount" REAL,
        "date" TEXT DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY("to_currency_code") REFERENCES "rates"("code"),
	    FOREIGN KEY("from_currency_code") REFERENCES "rates"("code")
    );
""" 

SQL_POPULATE_TABLE_RATES = F"""
INSERT INTO "{TABLE_RATES}" ("code", "rate_to_euro", "date")
values 
(?, ?, ?)

""" 
COUNTRY_PROPERTIES = ("continent_name", "country_code", "country_name","continent_code", "capital_name", "currency_code","phone_code", "three_letter_country_code")

SQL_POPULATE_TABLE_COUNTRIES = F"""
INSERT INTO "{TABLE_COUNTRIES}" ("continent_name", "country_code", "country_name","continent_code", "capital_name", "currency_code","phone_code", "three_letter_country_code")
values 
(?, ?, ?, ?, ?, ?, ?, ?)

""" 

SQL_GET_COUNTRY = F"""
SELECT * FROM {TABLE_COUNTRIES} WHERE upper(key) LIKE upper("%value%");
"""

# https://manage.exchangeratesapi.io/dashboard
# rates online

RATES_API = "4585446990311ad17f3ff45442c24766"
RATES_URL = F"http://api.exchangeratesapi.io/v1/latest?access_key={RATES_API}"
