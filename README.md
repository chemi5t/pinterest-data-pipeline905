Project Title
Table of Contents, if the README file is long
A description of the project: what it does, the aim of the project, and what you learned
Installation instructions
Usage instructions
File structure of the project
License information



# Pintrest Data Pipeline

# Table of Contents
- [A description of the project](#a-description-of-the-project)
- [Project Milestones - Summary](#project-milestones---summary)
    - [Outcomes from Milestone 1 (Setting up the environment):](#outcomes-from-milestone-1-setting-up-the-environment)
    - [Outcomes from Milestone 2 (Extracting and cleaning the data from the data sources):](#outcomes-from-milestone-2-extracting-and-cleaning-the-data-from-the-data-sources)
    - [Outcomes from Milestone 3 (Creating the database schema):](#outcomes-from-milestone-3-creating-the-database-schema)
    - [Outcomes from Milestone 4 (Querying the data):](#outcomes-from-milestone-4-querying-the-data)
- [Installation instructions](#installation-instructions)
- [Usage instructions](#usage-instructions)
- [File structure of the project](#file-structure-of-the-project)
- [Languages](#languages)
- [License information](#license-information)
- [Appendix](#appendix)
- [Project Milestones](#project-milestones)
    - [Milestone 1: Environment set up](#milestone-1-environment-set-up)
    - [Outcomes from Milestone 1 (Setting up the environment):](#outcomes-from-milestone-1-setting-up-the-environment-1)
    - [Milestone 2: Extract and clean the data from the data sources](#milestone-2-extract-and-clean-the-data-from-the-data-sources)
    - [Outcomes from Milestone 2 (Extracting and cleaning the data from the data sources):](#outcomes-from-milestone-2-extracting-and-cleaning-the-data-from-the-data-sources-1)
    - [Milestone 3: Create the database scheme](#milestone-3-create-the-database-scheme)
    - [Outcomes from Milestone 3 (Creating the database schema):](#outcomes-from-milestone-3-creating-the-database-schema-1)
    - [Milestone 4: Querying the data](#milestone-4-querying-the-data)
    - [Outcomes from Milestone 4 (Querying the data):](#outcomes-from-milestone-4-querying-the-data-1)

# A description of the project
The Multinational Retail Data Centralisation (MRDC) Project aims to address the challenge of their sales data being spread across many different data sources (AWS RSD, AWS S3 and API) and formats (PDF, CSV, and JSON). This hinders accessibility and analysis of the data. The project's primary objective is to establish a centralised database system that consolidates all sales data into a single location together with a star-based schema. This centralised repository will serve as the primary source of truth for sales data, enabling easy access and analysis for team members. The project involves storing up-to-date sales data in the database and developing querying mechanisms to generate the latest metrics for business analysis and decision-making.

In the `/root` (multinational-retail-data-centralisation) folder, the `main.py` file runs the various methods shown below that each perform the Extract, Transform, and Load (ETL) process for the six tables.

```python
if __name__ == "__main__":
    print("######################################## 1. ETL of Legacy Users ########################################")
    one_etl_legacy_users()

    print("######################################## 2. ETL of Card Details ########################################")
    two_etl_card_details()

    print("######################################## 3. ETL of Store Details ########################################")
    three_etl_store_details()

    print("######################################## 4. ETL of Product Details ########################################")
    four_etl_product_details()

    print("######################################## 5. ETL of Orders Details ########################################")
    five_etl_orders_details()

    print("######################################## 6. ETL of Date Events ########################################")
    six_etl_date_events()
```

The methods within the `main.py` script utilises the `data_cleaning.py`, `data_extraction.py`, and `database_utils.py` files and imports the DataCleaning, DataExtractor, and DatabaseConnector classes and uploads the clean data to the centralised database (`sales_data`) to complete the ETL pipeline.

A summary of the desired table extracted, from what source, connection method required and the name given to the table once uploaded to the database is given below:

        | Table Name       | Source              | Connection Method | Uploaded Table Name |
        |------------------|---------------------|-------------------|---------------------|
        | legacy_users     | AWS RDS database    | SQLAlchemy        | dim_users           |
        | card_details     | AWS S3 bucket (PDF) | tabula-py         | dim_card_details    |
        | store_details    | API                 | API requests      | dim_store_details   |
        | products_details | AWS S3 bucket (CSV) | boto3             | dim_products        |
        | orders_table     | AWS RDS database    | SQLAlchemy        | orders_table        |
        | date_details     | AWS S3 bucket (JSON)| boto3             | dim_date_times      |

The star-schema is completed by running `_05_SQL\_01_star_schema_sales_data.sql`, providing the Entity-Relationship Diagram (ERD) for the database. SQL is used to answer several business questions; the answers can be found in Milestone 4 or by running `_05_SQL\_02_queries.sql`.

This project provides an opportunity to gain insights into the logical structuring of `Python code` within `Visual Studio Code` (VS Code), an integrated development environment (IDE) commonly used for software development. With code management handled through `Git` and `GitHub`, version control and change tracking are streamlined, allowing for collaboration and easy rollback of changes.

Data extraction from various sources is managed efficiently using libraries such as `tabula-py`, `boto3`, and `SQLAlchemy`. These tools facilitate the retrieval of data from sources like `PDF` files and `AWS S3 buckets`, ensuring a seamless integration of data into the project pipeline. Additionally, `pandas` is employed for diverse data cleaning tasks, enabling the transformation and preparation of raw data for further processing.

The implementation of error handling mechanisms within the code ensures robustness, allowing for graceful handling of unexpected errors that may occur during script execution. `SQL` and `SQLTools` are utilised for writing and executing database queries, providing a powerful interface for interacting with the database backend.

Overall, this project offers a comprehensive learning experience encompassing various aspects of software development, data extraction, transformation, and database interaction. Through the utilisation of a diverse range of technologies and libraries, it equips individuals with the necessary skills to tackle real-world data-centric challenges effectively.

Finally, the scope for the MRDC project can be expanded in a number of way. To list a few:

1. After extraction of tables; to convert these saved `.csv` files to `.ipynb` files locally rather than direct from source. This would allow a more general function to to perform this task.
2. Perform extractions across the tables in one method, followed by clean and then upload. This may help with regard to bug fixing if required. 
3. Further factorising of code can occur. 
    - The saving of `.csv` and `.ipynb` could be made into a function and thus reducing lines of similar code.
    - The way pandas was used for cleaning of raw data from tables and its columns could have been generalised. Cleaning methods that dealt with certain tasks could have been generalised to handle a few tasks within a column and then called across various tables as needed. This would save on the number of coded lines and help the script look cleaner.
4. Private credentials have been accessed via two routes in the project, this could be changed to one style for consistency and minimise any credential related issues.  
5. A `.txt` file could have been generated out lining what cleans had been performed on the tables for auditing purposes. As it stands the user when running the `main.py` is able to read the output and get a general idea of how the data table looks before and after a clean via a print(df). A .txt output would enable the user to assess if other columns/factors had been or not been considered.


# Project Milestones - Summary
Refer to the appendix - Project Milestones, for a step-by-step guide on how the project was conducted. Here, you will find answers to several business questions that required querying the `sales_data` database using `SQLTools` and or `pgAdmin 4`.

## **Outcomes from Milestone 1 (Setting up the environment):**
Prerequisites and setup of laptop and `GitHub` were successful. The project can now be saved and tracked for changes via `Git` and `GitHub`. `VS Code` was used for writing the code.

## **Outcomes from Milestone 2 (Extracting and cleaning the data from the data sources):**
Milestone 2 continues from Milestone 1. The company's current up-to-date data is stored in a database locally titled `sales_data` in `pgAdmin 4` so that it is accessed from one centralised location and acts as a single point of reference for sales data. Data has been extracted from various sources in JSON, CSV, and PDF formats hosted on different platforms. Data was cleaned using `pandas` and stored in a local `PostgreSQL` database, `pgAdmin 4` using `SQLAlchemy`. Progress was updated to the repository on `GitHub` and code reviewed for better maintainability and efficiency.

A `db_cred.yaml` file was created containing the credentials and subsequently all other future sensitive information. This file was added to `.gitignore` to not upload any sensitive information to the public `GitHub` for security purposes.

Three classes were created in separate `Python` files:

DataExtractor class in `data_extraction.py` for extracting data from different sources.
DataCleaning class in `data_cleaning.py` for cleaning data extracted from different sources.
DatabaseConnector class in `database_utils.py` for connecting to and uploading data to the database.

These classes were all called within a `main.py` file where the ETL (Extract, Transform, Load) operations would occur. All the extracted tables were cleaned correctly by checking for NULL values, errors with dates, incorrectly typed values, unnecessary columns, and erroneous values. For the products_details table, the weights were converted to a common unit and cleaned. A summary of the desired table extracted, from what source, connection method required and the name given to the table once uploaded to the database is given below:

        | Table Name       | Source              | Connection Method | Uploaded Table Name |
        |------------------|---------------------|-------------------|---------------------|
        | legacy_users     | AWS RDS database    | SQLAlchemy        | dim_users           |
        | card_details     | AWS S3 bucket (PDF) | tabula-py         | dim_card_details    |
        | store_details    | API                 | API requests      | dim_store_details   |
        | products_details | AWS S3 bucket (CSV) | boto3             | dim_products        |
        | orders_table     | AWS RDS database    | SQLAlchemy        | orders_table        |
        | date_details     | AWS S3 bucket (JSON)| boto3             | dim_date_times      |

## **Outcomes from Milestone 3 (Creating the database schema):**
Milestone 3 continues from Milestone 2. Columns in the following tables were all cast to the correct data types using `SQL`, ensuring consistency and accuracy: orders_table, dim_users, dim_store_details, dim_products, dim_date_times, and dim_card_details.

It was found the dim_store_details table did not require merging the 'latitude' columns as the data in the 'lat' column has all been isolated and found to not be of use, and the column dropped.

Changes were made to the dim_products table via `SQL`; removal of '£' from the values of the 'product_price_(gbp)' column and adding a new 'weight_class' column. Also, a column name was altered from 'removed' to 'still available'. Upon changing this column data type to BOOL, it was found the values needed to be updated to reflect 'True' and 'False'. This is where an error was missed from the initial clean due to the values in this column containing 'Removed' and the incorrectly spelt 'Still_available'. The error shown via SQL during the updating of this table had drawn attention to the error that was then addressed.

Primary keys were added to dimension (dim) tables, establishing the foundation for the star-based schema. Foreign keys were created in the orders_table to reference primary keys in other dimension tables, completing the star-based schema. Latest code changes, including schema modifications, were pushed to the GitHub repository, and the README file was updated to reflect the project's progress and structure.

Entity-Relationship Diagram (ERD) for the `sales_data` database in `pgAdmin 4`:
>![ERD for database](_07_images\ERD.png)

## **Outcomes from Milestone 4 (Querying the data):**
Milestone 4 continues from Milestone 3. Now the schema for the database and all the sales_data is in one location. Queries were run against this for data-driven decisions and to get a better understanding of its sales. Below is an example of a question together with its answer. For all the questions tackled, refer to the appendix 'Milestone 4'. Otherwise see a few examples below: 

Task 1: How many stores does the business have and in which countries?
The Operations team would like to know which countries we currently operate in and which country now has the most stores. Perform a query on the database to get the information, it should return the following information:

            | country | total_no_stores |       
            |---------|-----------------|
            | GB      | 265             |
            | DE      | 141             |
            | US      | 34              |

            Note: DE is short for Deutschland (Germany)

Below was the searched query showing a match with the table above showing the total number of stores in each country where the business operates. This provided insight into the geographical distribution of the stores.

```sql
-- Task 1. How many stores does the business have and in which countries?
SELECT 
	country_code as country, 
	COUNT(country_code) as total_no_stores
FROM 
	dim_store_details
WHERE store_type != 'Web Portal'
GROUP BY 
	country_code
ORDER BY 
	total_no_stores DESC;
```
> ![M4T1](_07_images\M4T1.png)  

Task 5: What percentage of sales come through each type of store?
The sales team wants to know which of the different store types are generating the most revenue so they know where to focus. Find out the total and percentage of sales coming from each of the different store types. The query should return:

            | store_type  | total_sales | percentage_total(%) |
            |-------------|-------------|---------------------|
            | Local       | 3440896.52  | 44.87               |
            | Web portal  | 1726547.05  | 22.44               |
            | Super Store | 1224293.65  | 15.63               |
            | Mall Kiosk  | 698791.61   | 8.96                |
            | Outlet      | 631804.81   | 8.10                |

Below was the searched query showing a match with the table above showing the total sales and percentage contribution from the various store types, aiding in the focus of sales strategies.

```sql
-- Task 5. What percentage of sales come through each type of store?
WITH sum_of_sales AS (
    SELECT dsd.store_type, 
        ROUND(SUM(ot.product_quantity * dp."product_price_(gbp)")::numeric, 2) AS total_sales
    FROM dim_products AS dp
    JOIN orders_table AS ot ON dp.product_code = ot.product_code
    JOIN dim_store_details AS dsd ON ot.store_code = dsd.store_code
    GROUP BY dsd.store_type
),
total_sales_all AS (
    SELECT ROUND(SUM(ot.product_quantity * dp."product_price_(gbp)")::numeric, 2) AS total_sales
    FROM dim_products AS dp
    JOIN orders_table AS ot ON dp.product_code = ot.product_code
)
SELECT sum_of_sales.store_type, 
    ROUND(sum_of_sales.total_sales, 2) AS average_sum_of_payments, 
    ROUND((sum_of_sales.total_sales / total_sales_all.total_sales) * 100, 2) AS "percentage_total(%)"
FROM sum_of_sales
CROSS JOIN total_sales_all
ORDER BY average_sum_of_payments DESC;
```
> ![M4T5](_07_images\M4T5.png)  

Overall, this section focused on developing your skill over the understanding of `SELECT`, `JOIN`, `GROUP BY`, and aggregate functions. The ability to break down complex queries using subqueries and CTEs. Being able to aggregate data for insight. It developed competence in being able to manipulate data for meaningful insights. It allowed the ability to analyse trends and present findings visually. Familiarity was gained with the database schema structure, which made for more efficient querying. It helped with problem-solving skills in the capacity to interpret business needs and translate them into effective `SQL` queries. Overall, these skills empower efficient querying and help to facilitate informed decision-making.

# Installation instructions
From the main/root directory of the project folder, follow these steps:

1. cd into the directory and then in the command line:
    ```bash
    git clone https://github.com/chemi5t/multinational-retail-data-centralisation.git
    ```
2. Set up a virtual environment for the project:
    ```bash
    conda create --name mrdc_env
    ```
    ```bash
    conda activate mrdc_env
    ```
    ```bash
    pip install -r requirements.txt
    ```
- Packages of note:
    - boto3==1.34.21 
    - nbformat==5.9.2 
    - numpy==1.26.2 
    - pandas==2.1.3 
    - python-dateutil==2.8.2 
    - python-decouple==3.8 
    - PyYAML==6.0.1 
    - requests==2.31.0 
    - SQLAlchemy==2.0.23 
    - tabula-py==2.9.0
3. Set up a `PostgreSQL` database named `sales_data` using a client of your choice i.e. `pgAdmin 4`.
4. Save your database credentials to `db_creds.yaml` for security and to enable data extraction from various sources. Detailed instructions on setting up the database and configuring credentials can be found in Milestone 2.

# Usage instructions

1. Run the `main.py` to execute the data extraction, cleaning, and database creation processes in the `/root` folder via the terminal in `VS Code`.
    ```bash
    python main.py
    ```
2. Execute `_05_SQL\_01_star_schema_sales_data.sql` script via `pgAdmin 4` or `SQLTools` in `VS Code`; or any other tool you prefer for interacting with `PostgreSQL`. This sets up the star-schema in the `sales_data` database. ERD can be found in milestone 3.
3. Similarly run `_05_SQL\_02_queries.sql` which answers questions posed by the business by querying the `sales_data` database.

# File structure of the project

There are seven folders within the `/root` folder: 

- /_01_raw_tables_csv - *Raw untouched tables extracted via `main.py` and saved as `.csv`*
    - card_details.csv
    - date_details.csv
    - legacy_users.csv
    - orders_tabl.csv
    - products_details.csv
    - store_details.csv

- /_02_manipulate_raw_tables_ipynb - *Raw untouched tables extracted via `mian.py` and ready to be checked for cleaning*
    - card_details.ipynb
    - date_details.ipynb
    - legacy_users.ipynb
    - orders_tabl.ipynb
    - products_details.ipynb
    - store_details.ipynb

- /_03_cleaned_tables_csv - *Cleaned tables saved as `.csv` and uploaded to database automatically via `main.py`*
    - card_details_data_cleaned.csv
    - date_details_data_cleaned.csv
    - legacy_users_data_cleaned.csv
    - orders_tabl_data_cleaned.csv
    - products_details_data_cleaned.csv
    - store_details_data_cleaned.csv

- /_04_cleaned_tables_ipynb - *Files updated from folder `/_02*`. Tables cleaning logic saved `*_data_cleaned.ipynb`.*
    - card_details_data_cleaned.ipynb
    - date_details_data_cleaned.ipynb
    - legacy_users_data_cleaned.ipynb
    - orders_tabl_data_cleaned.ipynb
    - products_details_data_cleaned.ipynb
    - store_details_data_cleaned.ipynb

- /_05_SQL - *After running main.py the following `.sql` files set up the star-schema, provide answers to business questions and allows the removal of dependencies when starting over with re building the database*
    - _01_star_schema_sales_data.sql
    - _02_queries.sql
    - _03_drop_table_query.sql

- /_06_multinational_retail_data_centralisation - `*.py` files required by `main.py` to operate*
    - data_cleaning.py
    - data_extraction.py
    - database_utils.py

- /_07_images - *Picture files used in the `README.md`*
    - Contains image files

- /root - *This folder has all the folders seen above as well as containing the .env files which points to the stored private credentials.  `*.yaml`, `*.env`, and  `__pycache__/` have been added to `.gitignore`. Environment details saved to `requirements.txt`, `pip_requirements.txt` and `conda_requirements.txt`. `README.md` will also cover all aspects how the project was conducted over 4 milestones.* 
    - /_01_raw_tables_csv 
    - /_02_manipulate_raw_tables_ipynb
    - /_03_cleaned_tables_csv
    - /_04_cleaned_tables_ipynb
    - /_05_SQL
    - /_06_multinational_retail_data_centralisation
    - /_07_images 
    - .env
    - .gitignore
    - conda_requirements.txt
    - db_creds.yaml
    - main.py
    - pip_requirements.txt
    - README.md
    - requirements.txt

Screen shot of EXPLORER from `VS Code` containing the above contents:

> ![VSC1](_07_images\VSC1.png) 

# Languages

- Python
- SQL

# License information

This project is licensed under the terms of the [MIT License](LICENSE.md). Please see the [LICENSE.md](LICENSE.md) file for details.

# Appendix

