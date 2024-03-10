# Week 6 - File Ingestion and Schema Validation

1. Take any csv/text file of 2+ GB of your choice
2. Read the file (Present approach of reading the file)
3. Try different methods of file reading eg, Dask, Modin, Ray, pandas and present your findings in terms of computational efficiency
4. Perform basic validation on data columns: eg, remove special characters and white spaces from the col name
5. As you already know the schema, create a YAML file and write the column name in the YAML file. --define separator of read and write file, column name in YAML
6. Validate the number of columns and column name of an ingested file with YAML.
7. Write the file in pipe-separated text file (|) in gz format.
8. Create a summary of the file:
    - Total number of rows,
    - total number of columns
    - file size

## Dataset

I found the dataset(2GB) on Kraggle's site. You can also find on here: [Parking_Violations_Issued_-_Fiscal_Year_2017](https://www.kaggle.com/datasets/new-york-city/nyc-parking-tickets?select=Parking_Violations_Issued_-_Fiscal_Year_2017.csv).

*When you download the dataset and want to run this notebook, change the file path to yours.*
