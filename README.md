# NYC-Taxi-Cab-End-to-End-Pipeline
This project is focused on establishing a comprehensive end-to-end data pipeline for analyzing New York City taxi data. It employs a range of advanced technologies including Amazon S3 for storage, Mage for orchestration, Amazon EC2 for computational resources, AWS Glue for ETL processes, AWS Athena for querying, and Power BI for visualization. This well-rounded approach ensures the efficient extraction, transformation, loading, and analysis of taxi data, enabling stakeholders to derive valuable insights and make informed decisions.

![image](https://github.com/umergh7/NYC-Taxi-Cab-End-to-End-Pipeline/assets/117035545/c3a7facc-36c6-4842-8183-121bc7b77c7d)

## Step 1 - Source data via API
Sourcing NYC taxi data from the NYC.gov website and uploading it into an input S3 bucket

## Step 2 - Mage
Using Mage as the orchestration tool, I extracted the csv file from the input S3 bucket, and completed transformations to construct a fact table and respective dimension tables. The Mage orchestration tool is launched via a EC2 instance (medium). The pipeline extracts the csv file, completes transformations, and outputs the tables as a csv file onto an output S3 bucket.

## Step 3 - AWS Glue/Athena
AWS Glue is used to scan the S3 bucket, create a schema, and a table. Athena is used to query the table and it connects to PowerBI to create the visualizations.

## Step 4 - PowerBI
The PowerBI visualizations outline pickup locations, passenger counts, average trip distances, tip amount of day, and payment types. 

## Step 5 - Dashboard
![image](https://github.com/umergh7/NYC-Taxi-Cab-End-to-End-Pipeline/assets/117035545/e816fedc-fc62-4bf5-bc52-69782b363fb3)

