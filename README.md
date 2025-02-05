![image](https://github.com/user-attachments/assets/27ffb570-26fb-41c6-bb54-d5b96c98e076)

This repository contains an ETL (Extract, Transform, Load) pipeline designed to process sales data. The goal is to extract raw data, transform it according to business rules, and load it into a cloud database using modern and scalable tools.


**Project Objective**

The goal of this project is to build a robust ETL pipeline to process and analyze sales data. It covers all the steps of ETL:

1. **Extraction** : Collecting data from a CSV file with sales information.
2. **Transformation** : Applying calculations and categorizing data, including:
    - Calculation of total revenue per sale.
    - Classification of prices into categories ("Low", "Medium", "High").
3. **Loading** : Storing the transformed data in a cloud database (Google BigQuery).



## Technologies Used
- **Python** : Main language for pipeline development.
- **Apache Spark** : Distributed processing of large volumes of data.
- **Pandas** : In-memory data manipulation.
- **Google BigQuery** : Cloud data storage and analysis.
- **Git** : Code version control.
- **VSCode** : Integrated development environment.

## Repository Structure
- `data_generation/`: Contains the script for generating fictitious sales data.
  - [`generate_sales_data.py`](data_generation/generate_sales_data.py)
- `data_loading/`: Contains the script to load data into BigQuery.
  - [`to_big_query.py`](data_loading/to_big_query.py)
- `data_transformation/`: Contains the transformation script and the transformed data.
  - [`transform_sales_data.py`](data_transformation/transform_sales_data.py)
  - `transformed_data/`: Contains the transformed data.
    - [`transformed_sales_data.csv`](data_transformation/transformed_data/transformed_sales_data.csv)
- [`sales_data.csv`](sales_data.csv): Fictitious raw sales data.
- [`README.md`](README.md): Project documentation.
- [`requirements.txt`](requirements.txt): Project dependencies.
- [`gcp_key.json`](gcp_key.json): Authentication key for Google Cloud Platform.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/bsrikanth24/etl-pipeline-project-sales.git
   cd etl-pipeline-project-sales
   ```
2. Create and activate a virtual environment:
   ```py
   python -m venv venv
   source venv/bin/activate # On Windows use `venv\Scripts\activate`
   ```
3. Install the dependencies:
   ```sh
   pip install -r requirements.txt
  	```

## Usage

1. Generation of Fictitious Data:
   ```sh
   python data_generation/generate_sales_data.py
   ```
2. Data Transformation
   ```sh
   python data_transformation/transform_sales_data.py
   ```
3. Data Loading
   ```sh
   python data_loading/to_big_query.py
   ```

# BigQuery Load Breakdown

## Environment Configuration on GCP

1. Creating the Dataset in BigQuery:
   - Access the Google Cloud Platform console and create a dataset called sales_data for example.

2. Authentication Configuration:
   - Generate a JSON key for the project's service account on GCP.
   - Save the key as gcp_key.json in the root of the repository.
   - Set the environment variable in the terminal:
```sh
export GOOGLE_APPLICATION_CREDENTIALS=gcp_key.json
```
## Executing the to_big_query.py Script

1. Locate the Transformed File:
   - Make sure the transformed_sales_data.csv file is in the data_transformation/transformed_data/ folder.

2. Run the Script:
   
   ```sh   
   python data_loading/to_big_query.py
   ```
   	

3. Check the Output:

   ```sh
   Data successfully loaded into pipeline-project-sales.sales_data.transformed_sales_data table. Total rows: 100
   ```

4. Validation in the BigQuery Console:
   - Navigate to the sales_data dataset in GCP and open the transformed_sales_data table to validate the loaded data.


