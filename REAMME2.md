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

# Project Milestones - Summary
## **Outcomes from Milestone 1 (Setting up the environment):**
## **Outcomes from Milestone 2 (Extracting and cleaning the data from the data sources):**
## **Outcomes from Milestone 3 (Creating the database schema):**
## **Outcomes from Milestone 4 (Querying the data):**


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

## **Outcomes from Milestone 4 (Querying the data):**






# A description of the project
Pinterest crunches billions of data points every day to decide how to provide more value to their users. In this project, a similar system is created using the AWS Cloud.

# Summary of Project Milestones 
## **Outcomes from Milestone 1 (Setting up the environment):**
Prerequisites and setup of laptop and `GitHub` were successful. The project can now be saved and tracked for changes via `Git` and `GitHub`. `VSCode` was used for writing the code.

This project uses different services running in the AWS cloud and thus an AWS Cloud Account is required. 

## **Outcomes from Milestone 2 (Building the data pipeline via AWS):**

The Pinterest infrastructure is replicated, resembling the environment of a data engineer at Pinterest.

A user_posting_emulation.py script is developed, containing RDS database login credentials. The RDS database comprises three tables (pinterest_data, geolocation_data, and user_data) mimicking data obtained from user POST requests to Pinterest:

pinterest_data: Information about posts updated to Pinterest.
geolocation_data: Geographic data corresponding to posts in pinterest_data.
user_data: User information linked to posts in pinterest_data.
A db_creds.yaml file is created to store database credentials securely and excluded from version control using .gitignore.

The script continuously executes, emulating user posting behavior by connecting to the RDS database via SQLAlchemy. It fetches random rows from each table (pin_result, geo_result, and user_result), simulating user activity. Note the key-value pairing for later analysis.

Next, log into the AWS console keeping safe your:

Account ID: *
IAM user name: *
Password: *

When using any of the AWS services, make sure to work in us-east-1 region throughout this project.

## **Outcomes from Milestone 3 (Batch processing: Configuring the EC2 Kafka client):**

An `Amzon EC2` instance is used as an `Apache Kafka` clinet machine.

A `.pem` key is created locally which will allow you to connect to your `EC2` instance. To do this you navigate to the `Parameter Store` in your AWS account. Using your `KeyPairId` (this will be provided), find the specific key pair associated with your `EC2` instance. Select this key pair and under the 'Value' field, select 'Show decrypted value'. This will reveal the content of your key pair. Copy its entire value (including the BEGIN and END header) and paste it in the `.pem` file in `VSCode`.

Navigate to the EC2 console and identify the instance using the your UserId. Select this instance, and under the Details section find the `Key pair name` and make a note of this. Save the previously created file in the VSCode using the following format: Key pair name.pem.

Then connect to the EC2 instance. Follow the `Connect` instructions (SSH client) on the EC2 console to do this. NB. The .pem file is saved in the `home' folder under the Linus system via WSL.

Task 3: Set up Kafka on the EC2 instance

Your AWS account has been provided with access to an IAM authenticated MSK cluster. You don't have to create your own cluster for this project.
In order to connect to the IAM authenticated cluster, you will need to install the appropriate packages on your EC2 client machine.


Step 1:
First, install Kafka on your client EC2 machine.Don't worry about setting up the security rules for the EC2 instance to allow communication with the MSK cluster, as they have already been set up for you. Make sure to install the same version of Kafka as the one the cluster is running on (in this case 2.12-2.8.1), otherwise you won't be able to communicate with the MSK cluster.


Step 2:
Install the IAM MSK authentication package on your client EC2 machine. This package is necessary to connect to MSK clusters that require IAM authentication, like the one you have been granted access to.


Step 3:
Before you are ready to configure your EC2 client to use AWS IAM for cluster authentication, you will need to:

Navigate to the IAM console on your AWS account
Here, on the left hand side select the Roles section
You should see a list of roles, select the one with the following format: <your_UserId>-ec2-access-role
Copy this role ARN and make a note of it, as we will be using it later for the cluster authentication
Go to the Trust relationships tab and select Edit trust policy
Click on the Add a principal button and select IAM roles as the Principal type
Replace ARN with the <your_UserId>-ec2-access-role ARN you have just copied
By following the steps above you will be able to now assume the <your_UserId>-ec2-access-role, which contains the necessary permissions to authenticate to the MSK cluster.


Step 4:
Configure your Kafka client to use AWS IAM authentication to the cluster. To do this, you will need to modify the client.properties file, inside your kafka_folder/bin directory accordingly.


Task 4: Create Kafka topics

Step 1:
To create a topic, you will first need to retrieve some information about the MSK cluster, specifically: the Bootstrap servers string and the Plaintext Apache Zookeeper connection string. Make a note of these strings, as you will need them in the next step.


You will have to retrieve them using the MSK Management Console, as for this project you have not been provided with login credentials for the AWS CLI, so you will not be able to retrieve this information using the CLI.


Step 2:
You will need to create the following three topics:

<your_UserId>.pin for the Pinterest posts data
<your_UserId>.geo for the post geolocation data
<your_UserId>.user for the post user data
Before running any Kafka commands, remember to make sure your CLASSPATH environment variable is set properly.


In the create topic Kafka command replace the BootstrapServerString with the value you have obtained in the previous step.


You have been only granted permission to create topics with the exact names specified above on the MSK cluster. Please make sure you follow the format, otherwise you will run into permission errors.

Task 5: Begin documenting your experience

Document your progress by adding to your GitHub README file. You can refer to the relevant lesson in the prerequisites for this task for more information.

At minimum, your README file should contain the following information:

Project Title
Table of Contents, if the README file is long
A description of the project: what it does, the aim of the project, and what you learned
Installation instructions
Usage instructions
File structure of the project
License information
You don't have to write all of this at once, but make sure to update your README file as you go along, so that you don't forget to add anything.



An Amazon EC2 instance is utilised as an Apache Kafka client machine.
A local .pem key file is created to establish SSH connection with the EC2 instance.

Connect to the EC2 instance using SSH client instructions provided in the EC2 console.

Install Kafka and the IAM MSK authentication package on the client EC2 machine.
Retrieve and note the IAM role ARN (<your_UserId>-ec2-access-role) for cluster authentication.
Task 3: Configure Kafka client for IAM authentication
Modify the client.properties file in the Kafka installation directory to enable AWS IAM authentication.
Task 4: Create Kafka topics
Retrieve the Bootstrap servers string and the Plaintext Apache Zookeeper connection string from the MSK Management Console.
Create three topics: <your_UserId>.pin for Pinterest posts data, <your_UserId>.geo for post geolocation data, and <your_UserId>.user for post user data.
Task 5: Document your experience
Update the README file on GitHub with project title, description, installation and usage instructions, file structure, and license information.
Continuously update the README as you progress to ensure all relevant information is included.
This refined summary maintains the clarity and completeness of the original while providing a streamlined overview of the tasks involved in configuring the EC2 Kafka client.
















M4: Batch Processing: Connect a MSK cluster to a S3 bucket

You will use MSK Connect to connect the MSK cluster to a S3 bucket, such that any data going through the cluster will be automatically saved in a dedicated S3 bucket.

Task 1: Create a custom plugin with MSK Connect 

For this project you will not need to create a S3 bucket, an IAM role that allows you to write to this bucket or a VPC Endpoint to S3, as these have been already configured in your AWS account for you.


Step 1:
Go to the S3 console and find the bucket that contains your UserId. The bucket name should have the following format: user-<your_UserId>-bucket. Make a note of the bucket name, as you will need it in the next steps.


Step 2:
On your EC2 client, download the Confluent.io Amazon S3 Connector and copy it to the S3 bucket you have identified in the previous step.


Step 3:
Create your custom plugin in the MSK Connect console. For this project your AWS account only has permissions to create a custom plugin with the following name: <your_UserId>-plugin. Make sure to use this name when creating your plugin.

Task 2: Create a connector with MSK Connect 
For this project your AWS account only has permissions to create a connector with the following name: <your_UserId>-connector. Make sure to use this name when creating your connector.


Make sure to use the correct configurations for your connector, specifically your bucket name should be user-<your_UserId>-bucket.


You should also pay attention to the topics.regex field in the connector configuration. Make sure it has the following structure: <your_UserId>.*. This will ensure that data going through all the three previously created Kafka topics will get saved to the S3 bucket.


When building the connector, make sure to choose the IAM role used for authentication to the MSK cluster in the Access permissions tab. Remember the role has the following format <your_UserId>-ec2-access-role. This is the same role you have previously used for authentication on your EC2 client, and contains all the necessary permissions to connect to both MSK and MSK Connect.


Now that you have built the plugin-connector pair, data passing through the IAM authenticated cluster, will be automatically stored in the designated S3 bucket.

Task 3: Document

M5: Batch Processing: Congiuring an API in API Gateway

To replicate the Pinterest's experimental data pipline we will need to build our own API. This API will send data to the MSK cluster, which in turn will be stored in an S3 bucket, using the connector we have built in the previous milestone.

Task 1: Build a Kafka REST Proxy integration method for the API.

For this project you will not need to create your own API, as you have been provided with one already. The API name will be the same as your UserId.


Step 1:
Create a resource that allows you to build a PROXY integration for your API.


Step 2:
For the previously created resource, create a HTTP ANY method. When setting up the Endpoint URL, make sure to copy the correct PublicDNS, from the EC2 machine you have been working on in the previous milestones. Remember, this EC2 should have the same name as your UserId.


Step 3:
Deploy the API and make a note of the Invoke URL, as you will need it in a later task.

Task 2: Set up the Kafka REST proxy on the EC2 client

Now that you have set up the Kafka REST Proxy integration for your API, you need to set up the Kafka REST Proxy on your EC2 client machine.


Step 1:

First, install the Confluent package for the Kafka REST Proxy on your EC2 client machine.


Step 2:

Allow the REST proxy to perform IAM authentication to the MSK cluster by modifying the kafka-rest.properties file.


Step 3:

Start the REST proxy on the EC2 client machine.

Task 3: Send data to the API 

You are ready to send data to your API, which in turn will send the data to the MSK Cluster using the plugin-connector pair previously created.


Step 1:

Modify the user_posting_emulation.py to send data to your Kafka topics using your API Invoke URL. You should send data from the three tables to their corresponding Kafka topic.


Step 2:

Check data is sent to the cluster by running a Kafka consumer (one per topic). If everything has been set up correctly, you should see messages being consumed.


Step 3:

Check if data is getting stored in the S3 bucket. Notice the folder organization (e.g topics/<your_UserId>.pin/partition=0/) that your connector creates in the bucket. Make sure your database credentials are encoded in a separate, hidden db_creds.yaml file.

Task 4: document

M6: Batch processing: Databricks
You will set up your Databricks account and learn how to read data from AWS into Databricks.

Task 1: Set up your own Databricks account

When you launched your AWS account you had received a login email from Databricks. Follow the link in that email, as it will prompt you to the Databricks login page. Enter your email address (the same you have received the login email to) and select Forgot Password to set a new password. You should receive a second email with a link to follow to reset your password.

Task 2: Mount a S3 bucket to Databricks 

In order to clean and query your batch data, you will need to read this data from your S3 bucket into Databricks. To do this, you will need to mount the desired S3 bucket to the Databricks account. The Databricks account you have access to has already been granted full access to S3, so you will not need to create a new Access Key and Secret Access Key for Databricks. The credentials have already been uploaded to Databricks for you. You will only need to read in the data from the Delta table, located at dbfs:/user/hive/warehouse/authentication_credentials.

When reading in the JSONs from S3, make sure to include the complete path to the JSON objects, as seen in your S3 bucket (e.g topics/<your_UserId>.pin/partition=0/).


You should create three different DataFrames:

df_pin for the Pinterest post data
df_geo for the geolocation data
df_user for the user data.

Task 3: Document

Task 4: GitHub

Save the code you have created in Databricks to your local project repository.


Update your GitHub repository with the latest code changes from your local project. Start by staging your modifications and creating a commit. Then, push the changes to your GitHub repository.

M7: Batch Processing: Spark on Databricks

Learn how to perform data cleaning and computations using Spark on Databricks.

Task 1: Clean the DataFrame tha contains information about Pinterest posts.

To clean the df_pin DataFrame you should perform the following transformations:

Replace empty entries and entries with no relevant data in each column with Nones
Perform the necessary transformations on the follower_count to ensure every entry is a number. Make sure the data type of this column is an int.
Ensure that each column containing numeric data has a numeric data type
Clean the data in the save_location column to include only the save location path
Rename the index column to ind.
Reorder the DataFrame columns to have the following column order:
ind
unique_id
title
description
follower_count
poster_name
tag_list
is_image_or_video
image_src
save_location
category

Task 2: Clean the DF that contains information about geolocations.

To clean the df_geo DataFrame you should perform the following transformations:

Create a new column coordinates that contains an array based on the latitude and longitude columns
Drop the latitude and longitude columns from the DataFrame
Convert the timestamp column from a string to a timestamp data type
Reorder the DataFrame columns to have the following column order:
ind
country
coordinates
timestamp
Getting stuck on this task? 

Task 3: Clean the  DF that contains information about users.

To clean the df_user DataFrame you should perform the following transformations:

Create a new column user_name that concatenates the information found in the first_name and last_name columns
Drop the first_name and last_name columns from the DataFrame
Convert the date_joined column from a string to a timestamp data type
Reorder the DataFrame columns to have the following column order:
ind
user_name
age
date_joined

Task 4: Find the most popular category in each country.

Q1. Find the most popular Pinterest category people post to based on their country.


Your query should return a DataFrame that contains the following columns:

country
category
category_count, a new column containing the desired query output

Task 5: Find which was the most popular category each year.

Q2. Find how many posts each category had between 2018 and 2022.

    Your query should return a DataFrame that contains the following columns:
    
        post_year, a new column that contains only the year from the timestamp column
        category
        category_count, a new column containing the desired query output

Task 6: Find the user with the most followers in each coutnry.

Q3. Find the user with the most followers in each country.

    Step 1: For each country find the user with the most followers.

      Your query should return a DataFrame that contains the following columns:

      country
      poster_name
      follower_count
    
    Step 2: Based on the above query, find the country with the user with most followers.

      Your query should return a DataFrame that contains the following columns:

      country
      follower_count
      This DataFrame should have only one entry.

Task 7: Find the most popular category for different age groups.

    Q4. What is the most popular category people post to based on the following age groups:

      18-24
      25-35
      36-50
      +50

      Your query should return a DataFrame that contains the following columns:

      age_group, a new column based on the original age column
      category
      category_count, a new column containing the desired query output
      Getting stuck on this task? Click here to book a call to one of our support engineers

Task 8: Find the median follower count for different age groups.
    
    Q5. What is the median follower count for users in the following age groups:

      18-24
      25-35
      36-50
      +50
      
      Your query should return a DataFrame that contains the following columns:

      age_group, a new column based on the original age column
      median_follower_count, a new column containing the desired query output

Task 9: Q6. Find how many users have joined each year?
    Find how many users have joined between 2015 and 2020.

      Your query should return a DataFrame that contains the following columns:

      post_year, a new column that contains only the year from the timestamp column
      number_users_joined, a new column containing the desired query output



Task 10:  Q7. Find the median follower count of users based on their joining year.

    Find the median follower count of users have joined between 2015 and 2020.

      Your query should return a DataFrame that contains the following columns:

      post_year, a new column that contains only the year from the timestamp column
      median_follower_count, a new column containing the desired query output
      
Task 11: Q8. Find the median follower count of users based on their joining year and age group.

    Find the median follower count of users that have joined between 2015 and 2020, based on which age group they are part of.

      Your query should return a DataFrame that contains the following columns:

      age_group, a new column based on the original age column
      post_year, a new column that contains only the year from the timestamp column
      median_follower_count, a new column containing the desired query output

Task 12: document

Task 13: 
Save the queries you have created in Databricks to your local project repository.

Update your GitHub repository with the latest code changes from your local project. Start by staging your modifications and creating a commit. Then, push the changes to your GitHub repository.

M8: Batch Processing: AWS MWAA

You will orchestrate Databricks Workloads on AWS MWAA

Task 1: Create and upload a DAG to a MWAA enviroment

Your AWS account has been already been provided with access to a MWAA environment Databricks-Airflow-env and to its S3 bucket mwaa-dags-bucket. Thus, you will not be required to create an API token in Databricks to connect to your AWS account, to set up the MWAA-Databricks connection or to create the requirements.txt file.


You will only need to create an Airflow DAG that will trigger a Databricks Notebook to be run on a specific schedule. This DAG should be uploaded to the dags folder in the mwaa-dags-bucket.


Your AWS account has been granted permissions to upload and update the following file <your_UserId_dag.py> to the mwaa-dags-bucket. Make sure to give your DAG the correct name, otherwise you will run into permission errors. Be careful to also name the DAG inside the <your_UserId_dag.py> as such: <your_UserId_dag>. You should schedule the DAG to run daily.


Task 2: Trigger a DAG that runs a Databricks Notebook

Manually trigger the DAG you have uploaded in the previous step and check it runs successfully.

Task 3: document

Task 4: GitHub

Upload the DAG you have created from your local project repository to GitHub.


Update your GitHub repository with the latest code changes from your local project. Start by staging your modifications and creating a commit. Then, push the changes to your GitHub repository.

M9: Stream Processing: AWS Kinesis

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