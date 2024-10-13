Project Earthquake: A data pipeline to collate earthquake data
===
The following project has been created to apply to the position of Data Engineer at the company Pleo.

# Description
The task is to create a data pipeline that extracts data from [USGS](https://earthquake.usgs.gov/fdsnws/event/1/) and places it in BigQuery. This data needs to be 

What your application does,
Why you used the technologies you used,
Some of the challenges you faced and features you hope to implement in the future.

Create a data pipeline that finds all recorded earthquakes within 500 km of each of the pleo.io offices for the year to date and store the data in a target data warehouse (BigQuery). [Follow this link](https://docs.google.com/document/d/1xJ-x-0p4zXMwFO3c76kQdt0kvUdWElFVmLnPqXpBJm8/edit) to find the task.

[Architecture](link) -> TODO add image

## Goal
Create curated dataset with only following schema:

| column name         | Description     |
|--------------|-----------|
| time | Timestamp day of recorded earthquake |
| magnitude      | Recorded magnitude of earthquake  |
| latitude      | Latitude of earthquake  |
| longitude      | Longitude of earthquake  |
| place      | Address from where earthquake happened  |
| hased_id      | Hashed ID using all columns of the raw dataset  |
| location      | Name of the extract location  |
| inserted_at      | Timestamp of the extracted data  |

> Additional columns: hased_id, location, inserted_at were added to enrich the dataset further.

## Deliverables
1. Deployable in production
2. Tests have been added
3. Scheduled query that should run once a week
4. Explanation of how to run the service and test it
5. Suggestions on next steps on how to build a more robust infrastructure

## Learnings
- How to work with unittests and the mock module
- Working with GCP BigQuery
  - Creating projects & datasets
  - Managing service accounts secrets
- Creating logical logging mechanisms for debugging
- Packaging project ready for deployment: working with docker & Makefile


# How to install
The following section will run you through on how to deploy locally. There are no preqrequisites for this project, because everything is packages in the Dockerfile and it can be deployed using the Makefile.

1. Clone the repository.
2. Create a project for this app in BigQuery.
3. In the newly created project, create the datasets: `raw_data` and `curated_data` in BigQuery.
4. In the app.py update the "BigQuery parameters" as per the ones set by you.
5. Create a service account in the newly created project.
6. Place the service account in the root directory and rename it to `bigquery-project-earthquake-secrets.json`
8. Run the Makefile with `make prod`.

# Run tests
Find the tests you want to run and call them with the function
```
python -m unittest tests/{file_name}.py
```
