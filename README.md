# Pinterest Data Pipeline

# A description of the project

Pinterest, a popular social media platform and visual discovery engine, allows users to save and share ideas through images and videos known as "pins." Users organise their pins into themed collections called "boards," covering diverse topics like home decor, fashion, recipes, and more. With vast data storage and processing billions of data points daily, Pinterest aims to enhance user experience by leveraging data insights.

This project aims to replicate Pinterest's data processing system by creating an end-to-end pipeline on the AWS Cloud. The pipeline orchestrates data ingestion, storage, and real-time analysis, utilising a range of technologies:

- Amazon Elastic Compute Cloud (EC2) for computing resources
- Amazon Simple Storage Service (S3) for scalable object storage
- SQL for data querying and manipulation
- Apache Kafka/AWS Managed Streaming for Apache Kafka (MSK) for streaming data processing
- Amazon API Gateway for creating APIs
- Spark for distributed data processing
- Databricks for data engineering and analytics
- Amazon Managed Workflows for Apache Airflow (MWAA) for workflow orchestration
- Amazon Kinesis for real-time data streaming

By leveraging these technologies, this project aims to demonstrate how to build a secure, robust and scalable data processing pipeline similar to that of Pinterest via AWS Cloud. Additionally, the pipeline facilitates value extraction through SQL queries, enhancing the project's analytical capabilities.


# Installation instructions
From the main/root directory of the project folder, follow these steps:

1. cd into the directory and then in the command line:
    ```bash
    git clone https://github.com/chemi5t/pinterest-data-pipeline905.git
    ```
2. Set up a virtual environment for the project:
    ```bash
    conda create --name pinterest_env
    ```
    ```bash
    conda activate pinterest_env
    ```
    ```bash
    pip install -r requirements.txt
    ```
- Packages of note:                 ########### update this ###########
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
3. Create and set up AWS and Databricks accounts.
4. Save your database credentials to `db_creds.yaml` for security and to enable data extraction/uploads from/to various sources. Detailed instructions on setting these up and configuring credentials can be found wothin the Milestones explained later.

that contains only the year from the timestamp column
      number_users_joined, a new column containing the desired query output


# Summary of Project Milestones 

## Data Emulation:

- ### **Outcomes from Milestone 1 (Setting up the environment)**

`GitHub` was successfully set up to allow the project to be saved and tracked for changes via `Git` and `GitHub`. `VSCode` was used for writing the code.

This project uses different services running in the AWS Cloud and thus an AWS Cloud Account is required. 

- ### **Outcomes from Milestone 2 (Creating Pinterest infrastructure via AWS RDS database)**

The Pinterest infrastructure is replicated to resemble the environment of a data engineer at Pinterest. 

A `user_posting_emulation_basic.py` script is developed, containing RDS database login credentials. The RDS database comprises three tables (pinterest_data, geolocation_data, and user_data) mimicking data obtained from user POST requests to Pinterest:

`pinterest_data`: Information about posts updated to Pinterest.
`geolocation_data`: Geographic data corresponding to posts in `pinterest_data`.
`user_data`: User information linked to posts in `pinterest_data`.

A `db_creds.yaml` file is created to store database credentials securely and excluded from version control using .gitignore.

The script continuously executes, emulating user posting behavior by connecting to the RDS database via SQLAlchemy. It fetches random rows from each table (pin_result, geo_result, and user_result), simulating user activity. The key-value pairing in the dictionaries are noted for later analysis.

```python
(base) 
chemi@DELL-laptop MINGW64 ~/AiCore_Projects/pinterest-data-pipeline905 (main)
$ python user_posting_emulation_basic.py 
**************************************************
pin result:  {'index': 7528, 'unique_id': 'fbe53c66-3442-4773-b19e-d3ec6f54dddf', 'title': 'No Title Data Available', 'description': 'No description available Story format', 'poster_name': 'User Info Error', 'follower_count': 'User Info Error', 'tag_list': 'N,o, ,T,a,g,s, ,A,v,a,i,l,a,b,l,e', 'is_image_or_video': 'multi-video(story page format)', 'image_src': 'Image src error.', 'downloaded': 0, 'save_location': 'Local save in /data/mens-fashion', 'category': 'mens-fashion'}

geo result:  {'ind': 7528, 'timestamp': datetime.datetime(2020, 8, 28, 3, 52, 47), 'latitude': -89.9787, 'longitude': -173.293, 'country': 'Albania'}

user result:  {'ind': 7528, 'first_name': 'Abigail', 'last_name': 'Ali', 'age': 20, 'date_joined': datetime.datetime(2015, 10, 24, 11, 23, 51)}
**************************************************
```

Next, log into the AWS console keeping safe your credentials:

- AWS Account ID: <your_AWSId>
- IAM user name: <your_UserId>
- Password: <your_Password>
- The above are values to be replaced by your own and where ever mentioned herein

When using any of the AWS services, make sure to work in `us-east-1` region throughout the project.

## Batch Processing:

- ### **Outcomes from Milestone 3 (Batch processing: Configuring the EC2 Kafka client)**

Install `Kafka` and the `IAM MSK authentication package` on the client `EC2` machine.
Retrieve and note the `IAM role ARN` (<your_UserId>-ec2-access-role) for cluster authentication.
Configure `Kafka` client for `IAM authentication`. Modify the `client.properties` file in the `Kafka` installation directory to enable `AWS IAM authentication`.
Create `Kafka` topics by retrieving the `Bootstrap servers` string and the Plaintext `Apache Zookeeper` connection string from the `MSK` Management Console.
Create three topics: 
- `<your_UserId>.pin` for Pinterest posts data, 
- `<your_UserId>.geo` for post geolocation data, and 
- `<your_UserId>.user` for post user data.

For further details follow - [Milestone 3 outline](documentations/milestone_3.md)

- ### **Outcomes from Milestone 4 (Batch Processing: Connect a MSK cluster to a S3 bucket)**

For this project it was not required to create a S3 bucket, an IAM role that allows you to write to this bucket or a VPC Endpoint to S3, as these had already been configured for the AWS account.

In this milestone, MSK Connect is utilised to establish a connection between the MSK cluster and an S3 bucket, enabling automatic data storage for all cluster data.

A custom plugin is created with `MSK Connect`.
Navigate to the `S3` console and locate the bucket associated with your <your_UserId> (`user-<your_UserId>-bucket`).
Download the `Confluent.io Amazon S3 Connector` on your `EC2` client and transfer it to the identified `S3` bucket.
Create a custom plugin named `<your_UserId>-plugin` in the `MSK Connect` console.
Create a connector with `MSK Connect` named `<your_UserId>-connector` in the `MSK Connect` console.
Configure the connector with the correct bucket name (`user-<your_UserId>-bucket`) and ensure the `topics.regex` field follows the format `<your_UserId>.*`.
Assign the `IAM role` used for authentication to the MSK cluster (`<your_UserId>-ec2-access-role`) in the Access permissions tab.
Upon completing these tasks, data passing through the `IAM authenticated` cluster will be automatically stored in the designated `S3` bucket.

For further details follow - [Milestone 4 outline](documentations/milestone_4.md)

- ### **Outcomes from Milestone 5 (Batch Processing: Configuring an API in API Gateway):**
This milestone focuses on building an API to replicate Pinterest's experimental data pipeline. The API will send data to the MSK cluster, which will then be stored in an S3 bucket using the previously configured connector.

A Kafka REST proxy integration method is built for the API. A resource is created for the API to enable a PROXY integration.
A HTTP ANY method is set up for the resource, ensuring the Endpoint URL reflects the correct PublicDNS of the EC2 machine associated with <your_UserId>.
The API is deployed and the Invoke URL noted for future reference.

The Kafka REST proxy is set up on the EC2 client by installing the Confluent package for the Kafka REST proxy on the EC2 client machine.
The kafka-rest.properties file is configured to allow the REST proxy to perform IAM authentication to the MSK cluster.
The REST proxy on the EC2 client machine is started.
Then send data to the API after modifying the `user_posting_emulation_basic.py` script to `user_posting_emulation_batch.py` and send data to the Kafka topics via the `API Invoke URL`.
Confirm data storage in the `S3` bucket, observing the folder organisation created by the `connector`.

For further details follow - [Milestone 5 outline](documentations/milestone_5.md)

- ### **Outcomes from Milestone 6 (Batch processing: Databricks)**
This milestone focuses on setting up a `Databricks` account and learning to read data from `AWS` into `Databricks`.

Set up your own `Databricks` account followed by mounting the previously created `S3` bucket to `Databricks`.
Mount the desired S3 bucket to the Databricks account to access the batch data.
The `Databricks` account has full access to `S3`, eliminating the need to create a new `Access Key` and `Secret Access Key`.
Read data from the `Delta table` located at `dbfs:/user/hive/warehouse/authentication_credentials`.
Ensure complete paths to `JSON` objects when reading from `S3` (e.g. topics/<your_UserId>.pin/partition=0/).
Create three DataFrames: 

- `df_pin` for Pinterest post data
- `df_geo` for geolocation data
- `df_user` for user data

This summary outlines the tasks involved in configuring `Databricks`, mounting an `S3` bucket and reading data.

For further details follow - [Milestone 6 outline](databricks/_1_mount_s3_to_databricks.ipynb)

- ### **Outcomes from Milestone 7 (Batch processing: Spark on Databricks)**

Perform data cleaning and computations using Spark on Databricks. Apply this to all 3 PySpark DataFrames:

- `df_pin` for Pinterest post data
- `df_geo` for geolocation data
- `df_user` for user data

For further details follow - [Milestone 7 df cleaning outline](databricks/_2_batch_data_processing_from_mounted_s3.ipynb)

It was also demonstrated how valuable insights could be produced by joining the 3 dataframes via the execution of SQL queries.

For further details follow - [Milestone 7 SQL queries](databricks/_3_pinterest_queries.ipynb)


- ### **Outcomes from Milestone 8 (Batch processing: AWS MWAA)**

Databricks Workloads are orchestrated on AWS MWAA (Managed Workflows for Apache Airflow).

Task 1: Create and upload a DAG to a MWAA enviroment

Your AWS account has been already been provided with access to a MWAA environment Databricks-Airflow-env and to its S3 bucket mwaa-dags-bucket. Thus, you will not be required to create an API token in Databricks to connect to your AWS account, to set up the MWAA-Databricks connection or to create the requirements.txt file.


You will only need to create an Airflow DAG that will trigger a Databricks Notebook to be run on a specific schedule. This DAG should be uploaded to the dags folder in the mwaa-dags-bucket.


Your AWS account has been granted permissions to upload and update the following file `<your_UserId>_dag.py` to the mwaa-dags-bucket. Make sure to give your DAG the correct name, otherwise you will run into permission errors. Be careful to also name the DAG inside the <your_UserId_dag.py> as such: <your_UserId_dag>. You should schedule the DAG to run daily.


Task 2: Trigger a DAG that runs a Databricks Notebook

Manually trigger the DAG you have uploaded in the previous step and check it runs successfully.

Task 3: document

Task 4: GitHub

Upload the DAG you have created from your local project repository to GitHub.


Update your GitHub repository with the latest code changes from your local project. Start by staging your modifications and creating a commit. Then, push the changes to your GitHub repository.

## Stream Processing:

- ### **Outcomes from Milestone 9 (Stream Processing: AWS Kinesis)**

Send streaming data to Kinesis and read this data in Databricks

Task 1: Create data streams using Kinesis Data Streams

Using Kinesis Data Streams create three data streams, one for each Pinterest table.


Your AWS account has only been granted permissions to create and describe the following streams:

streaming-<your_UserId>-pin
streaming-<your_UserId>-geo
streaming-<your_UserId>-user
Make sure you follow the correct nomenclature, otherwise you will run into permission errors when creating the streams.

Task 2: Configure an API with Kinesis proxy integration

Configure your previously created REST API to allow it to invoke Kinesis actions. Your AWS account has been granted the necessary permissions to invoke Kinesis actions, so you will not need to create an IAM role for your API to access Kinesis.


The access role you have been provided with has the following structure: <your_UserId-kinesis-access-role>. You can copy the ARN of this role from the IAM console, under Roles. This is the ARN you should be using when setting up the Execution role for the integration point of all the methods you will create.


Your API should be able to invoke the following actions:

List streams in Kinesis
Create, describe and delete streams in Kinesis
Add records to streams in Kinesis

Task 3: Send data to the Kinesis streams

Create a new script user_posting_emulation_streaming.py, that builds upon the initial user_posting_emulation.py you have been provided with.


In this script, you should send requests to your API, which adds one record at a time to the streams you have created. You should send data from the three Pinterest tables to their corresponding Kinesis stream.


Make sure your database credentials are encoded in a separate, hidden db_creds.yaml file.

Task 4: Read data from Kinesis streams in Databricks

Step 1:
Create a new Notebook in Databricks and read in your credentials from the Delta table, located at dbfs:/user/hive/warehouse/authentication_credentials, to retrieve the Access Key and Secret Access Key. Follow the same process for this, as you have followed for your batch data.


Step 2:

Run your preferred method to ingest data into Kinesis Data Streams. In the Kinesis console, check your data streams are receiving the data.


Step 3:

Read the data from the three streams you have created in your Databricks Notebook.

Task 5: Transforms orm Kinesis streams in Databricks

Clean the streaming data in the same way you have previously cleaned the batch data.

Task 6: Write the streaming data to Delta Tables

Once the streaming data has been cleaned, you should save each stream in a Delta Table. You should save the following tables: <your_UserId>_pin_table, <your_UserId>_geo_table and <your_UserId>_user_table.

Task 7: Document your exp

Task 8: GitHub

Save the code you have created in Databricks to your local project repository.


Update your GitHub repository with the latest code changes from your local project. Start by staging your modifications and creating a commit. Then, push the changes to your GitHub repository.

Finally, you can upload the diagram of the architecture you created using this template .

# Usage instructions

1. Batch processing
2. Steam Processing
3. Data Querying 

<!-- 1. Run the `main.py` to execute the data extraction, cleaning, and database creation processes in the `/root` folder via the terminal in `VS Code`.
    ```bash
    python main.py
    ```
2. Execute `_05_SQL\_01_star_schema_sales_data.sql` script via `pgAdmin 4` or `SQLTools` in `VS Code`; or any other tool you prefer for interacting with `PostgreSQL`. This sets up the star-schema in the `sales_data` database. ERD can be found in milestone 3.
3. Similarly run `_05_SQL\_02_queries.sql` which answers questions posed by the business by querying the `sales_data` database. -->

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

<!-- - Python
- SQL -->

# License information

<!-- This project is licensed under the terms of the [MIT License](LICENSE.md). Please see the [LICENSE.md](LICENSE.md) file for details. -->





