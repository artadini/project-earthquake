# Project Earthquake: A data pipeline to collate earthquake data
Create a data pipeline that finds all recorded earthquakes within 500 km of each of the pleo.io offices for the year to date and store the data in a target data warehouse.

## Goal
Store the clean data and the following columns in a target table:
* date and time
* magnitude
* latitude
* longitude
* Place

# Description
The task is to create a data pipeline that extracts data from [USGS](https://earthquake.usgs.gov/fdsnws/event/1/) and places it in BigQuery. This data needs to be 

## Requirements to deliver this project:
[] Deployable in production
[] Tests have been added
[] Scheduled query that should run once a week
[] Explanation of how to run the service and test it
[] Suggestions on next steps on how to build a more robust infrastructure

Notes:
Links have been added to the databases' name
https://docs.google.com/document/d/1xJ-x-0p4zXMwFO3c76kQdt0kvUdWElFVmLnPqXpBJm8/edit

# How to run this project
1. Clone the repository.
2. Create a project in your BigQuery instance and set the service account up.
3. Place the service account in the root directory.
4. Rename the service account file to `bigquery-project-earthquake-secrets.json`.
6. Run the Dockerfile to set the environment up.

# Learnings
