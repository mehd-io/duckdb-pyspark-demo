# DuckDB & Pyspark Demo
This repository serves as a practical demonstration of leveraging the DuckDB engine while maintaining the same PySpark code pipeline `duckspark.py`, thanks to DuckDB's compatibility with the PySpark API. It provides a comparative analysis of a standalone PySpark pipeline versus a PySpark pipeline powered by DuckDB, using an openly available dataset. The entire setup is containerized for ease of deployment and quick startup.

## Disclaimer
⚠️ Please note that this feature is experimental. For details on what's available from the PySpark API, please visit DuckDB's GitHub repository.

## Getting Started
### Prerequisites
Before diving into the demo, ensure you have **Docker** installed on your system. This demo relies on Docker containers to run the PySpark and DuckDB environments.

### Download the Data
Run the following command to download the necessary dataset. It contains Hacker News data for about ~1GB in Parquet.
```
make data
```

## Running the Demos
After setting up, you can run the demos using the following commands. Each commands use container and target the same codebase `duckspark.py`.

**DuckDB with PySpark**
To run the demo using DuckDB with PySpark, execute the following command. This command builds the Docker image (if not already built) and runs the script using DuckDB.
```
make duckspark
```

result:
```
real	0m0.260s
user	0m0.561s
sys	    0m0.040s
```

**Standalone PySpark**
```
make pyspark
```

result : 
```
real	0m2.239s
user	0m4.520s
sys	0m0.353s
```

These commands will execute the respective pipelines and display the time taken for each process, allowing you to compare the performance between the pure PySpark implementation and the DuckDB version.
